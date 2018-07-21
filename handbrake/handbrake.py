#!/usr/bin/python3

import argparse
import sys
import json
import re

parser = argparse.ArgumentParser(prog='test')
parser.add_argument('--season', help='number of season', type=int)
parser.add_argument('--start', help='number of first episode', type=int)
parser.add_argument('--end', help='number of last episode', type=int)

parser.add_argument('--output', help='output file path')
parser.add_argument('--input', help='input file path')

parser.add_argument('--profile', help='path to handbrake json file (queue file)')
parser.add_argument('--json', help='path where handbrake json file will be written')

parser.add_argument('--debug', help='get text instead json', dest='debug', action='store_true')

args = parser.parse_args()


if not (args.profile and  args.input and args.output):
	print("missing parameters")
	sys.exit(1)

with open(args.profile) as j:
	data = json.load(j)

# first entry will be used as profile
first_entry = data[0]

raw_pathes = {
	'src': ('%s' % args.input),
        'dst': ('%s' % args.output)
}

# every file to enqueue
output = list()

# start to end
for x in range(args.start, int(args.end)+1):
	data = first_entry

	pathes = {
		'src': {},
		'dst': {}
	}

	# substitution of placeholders
	for i, p in raw_pathes.items():
		raw_path = p

		if '__e__' in p:
			 raw_path = raw_path.replace('__e__', x)
		if '__s__' in p:
			raw_path = raw_path.replace('__s__', int(args.season))
		if '__ee__' in p:
			raw_path = raw_path.replace('__ee__', '%02d' % x)
		if '__ss__' in p:
			raw_path = raw_path.replace('__ss__', '%02d' % int(args.season))

		pathes[i] = raw_path

	# maybe you want to check dst / src path before generating json
	if args.debug:
		print(pathes)
		continue

	data['Job']['Source']['Path'] = pathes['src']
	data['Job']['Destination']['File'] = pathes['dst']

	output.append(data)

# write queue to json file
if args.json:
	with open(args.json, 'w') as outfile:
		json.dump(output, outfile)
	sys.exit(0)

# print out json structure
print(json.dumps(output))

