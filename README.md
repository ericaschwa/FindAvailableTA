# FindAvailableTA

Uses web scraping from the TA website and returns the TA that is on duty at the current time.

Takes optional day and time argument; if none is given, defaults to current day of the week and time in EST.

## Usage:

python findta.py

OR

python findta.py `day` `time`

`day` must be one of the following:
- `M`
- `T`
- `W`
- `R`
- `F`
- `S`
- `U`

`time` is a time given in military format, in EST. Examples include `0800` and `1615`.
