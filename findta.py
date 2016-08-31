import sys
import datetime
from datetime import datetime
import time

from pytz import timezone
import lxml
from lxml import html
import requests


def findTA(day, timeOfDay):
	"""
	Given a day and time, finds the TA available, and returns the TA's name
	If no TAs are available, returns None
	"""
	page = requests.get('http://www.cs.tufts.edu/comp/15/admin.shtml')
	tree = html.fromstring(page.content)

	# hard-coded for now, will be from site once this info is available
	# times for the given day
	times = {
		'0900': 'Erica',
		'1030': 'Foo',
		'1200': 'Bar',
		'1330': 'FooBar',
		'1500': 'LALAFooFoo',
		'1630': 'DinnerTimeTA',
		'1800': 'NapTimeTA',
		'1930': 'Chaos',
		'2100': 'TAHERE',
		'2230': 'TANOTHERE',
		'2400': 'LOLNO'
	}

	for time in times.keys():
		if time <= timeOfDay and str(int(time) + 150) >= timeOfDay:
		   	return times[time]
	return None


def main():
	"""
	Processes command line args to retrieve desired date and time
    If none are given, defaults to now
	"""
	if len(sys.argv) > 2:
		day = sys.argv[1]
		timeOfDay = sys.argv[2]

	else:
		local_tz = timezone(time.tzname[0])
		EST_tz = timezone('EST')
		timeWithTZ = local_tz.localize(datetime.now())
		EST_time = timeWithTZ.astimezone(EST_tz).time()
		timeOfDay = EST_time.isoformat().split(':')[0] + \
					EST_time.isoformat().split(':')[1]

		weekdays = ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat']
		day = weekdays[timeWithTZ.weekday()]

	print findTA(day, timeOfDay)


if __name__ == "__main__":
    main()