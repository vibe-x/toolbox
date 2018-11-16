#!/usr/bin/env python3

import glob, os, sys
import argparse

from mutagen import File
from mutagen.flac import Picture


parser = argparse.ArgumentParser(description='replace low quality picture in flac file with better')
parser.add_argument('--path', help='path to scan for files')

args = parser.parse_args()

directory = args.path

if not directory or not os.path.isdir(directory):
	print("directory [%s] does not exist" % directory )
	sys.exit(1)

for d in glob.glob(directory + "/*"):
	# skip files in root directory
	if not os.path.isdir(d):
		continue

	cover = None
	# get the cover (use the first image found in directory)
	for f in glob.glob(d + "/*.jp*g"):
		cover = f
		break

	if not cover:
		print("no cover found in directory [%s]" %d)
		sys.exit(1)

	# scan for flac files
	for flac in glob.glob(d + "/*.flac"):
		# create mutagen picture object
		pic = Picture()

		# open cover file and store into flac file
		with open(cover, "rb") as c:
			# read raw picture data from cover file
			pic.data = c.read()

			mfile = File(flac)
			# remove old and add new cover
			mfile.clear_pictures()
			mfile.add_picture(pic)
			mfile.save()
