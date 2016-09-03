import sys
import datetime
from datetime import datetime
import time

from pytz import timezone
import lxml
from lxml import html
import requests

def getTimes(tree):
    """
    Give the html tree of a webpage, finds the listing of TA availability and
    returns a dict containing this information
    """
    # hard-coded for now, will be from site once this info is available
    # times for the given day
    return {
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


def findTA(day, timeOfDay):
    """
    Given a day and time, finds the TA available, and returns the TA's name
    If no TAs are available, returns None
    """
    page = requests.get('http://www.cs.tufts.edu/comp/15/admin.shtml')
    tree = html.fromstring(page.content)
    times = getTimes(tree)

    for time in times.keys():
        if time <= timeOfDay:
            if time[2] == '0' and str(int(time) + 130) > timeOfDay:
                return times[time]
            elif time[2] == '3' and str(int(time) + 170) > timeOfDay:
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
        timeWithTZ = local_tz.localize(datetime.now())
        EST_tz = timezone('EST')
        EST_time = timeWithTZ.astimezone(EST_tz)
        timeOfDay = EST_time.time().isoformat().split(':')[0] + \
                    EST_time.time().isoformat().split(':')[1]

        weekdays = ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat']
        day = weekdays[EST_time.weekday()]

    print findTA(day, timeOfDay)


if __name__ == "__main__":
    main()
