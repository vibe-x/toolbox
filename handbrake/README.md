# Handbrake Helper

You can use this to create queue files, which can be processed by handbrake-cli.

## Parameters


#### profile (json)

This will load the default configuration for the batch job. You can (should) export your custom settings via handbrake queue to ensure your settings are fine.

```--profile /path/to/queue.json```


#### queue output(json)

The file will be created and contains the wanted jobs (start => end).

```--json /path/to/output.json```


#### range

Range of files, where input iteration will goes from 0 till 6, output 1 till 7 (because of offset).

```--start 0 --end 6 --offset 1```


#### input / output

path / file syntax with templating functionality. The combination of pathes depends on handbrake.

```
--input '\\path\to\windows\share\series.mkv
--output '\\path\to\windows\share\destination.mkv'

--input '/home/user/movies/series.mkv'
--output '/home/user/my_destination/dest.mkv'
```

You can use:

```
__e__ episode counter (1, 2, [...], end)
__ee__ episode counter (01, 02, [...], end)
__s__ season number (1)
__ss__ season number with leading zero
```

## Example

```
./handbrake.py --json /home/user/video/encode.json --profile /home/user/video/queue.json --start 1 --end 6 --season 1 --input '/home/user/series_raw/superhuman.S__ss__E__ee__.2018.mkv' --output '/home/user/series/sh__ss__/superhuman.S__ss__E__ee__.2018.mkv'
```
