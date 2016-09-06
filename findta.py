import sys
import datetime
from datetime import datetime
import time

from pytz import timezone
import lxml
from lxml import html
import requests


def printTas(tas):
    """
    Given a list of TAs, prints the list
    """
    if len(tas) > 0:
        print "The TAs on duty are:"
        for ta in tas:
            print ta


def getTimes(tree, day):
    """
    Give the html tree of a webpage, finds the listing of TA availability and
    returns a dict containing this information
    """

    # http://docs.python-guide.org/en/latest/scenarios/scrape/
    pres = tree.xpath('//pre/text()')

    tas = pres[0].split('Schedule by TA')[1].split('\n')[2:-2]
    timedict = {'M': {}, 'T': {}, 'W': {}, 'R': {}, 'F': {}, 'U': {}}

    for ta in tas:
        taName = ta.split(':')[0].split()[0]
        taTimes = ta.split(':')[1].split(', ')
        for time in taTimes:
            if time[1:] in timedict[time[0]]:
                timedict[time[0]][time[1:]].append(taName)
            else:
                timedict[time[0]][time[1:]] = [taName]

    return timedict[day]


def findTA(day, timeOfDay):
    """
    Given a day and time, finds the TA available, and returns the TA's name
    If no TAs are available, returns None
    """
    page = requests.get('http://www.cs.tufts.edu/comp/15/admin.shtml')
    tree = html.fromstring(page.content)
    times = getTimes(tree, day)

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

        weekdays = ['U', 'M', 'T', 'W', 'R', 'F', 'S']
        day = weekdays[EST_time.weekday()]

    tas = findTA(day, timeOfDay)
    printTas(tas)


if __name__ == "__main__":
    main()
