import sys
import datetime
from datetime import datetime
from pytz import timezone
import time


def findTA(day, timeOfDay):
	return (day, timeOfDay)

def main():

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