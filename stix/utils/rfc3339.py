
# rfc3339.py -- Implementation of the majority of RFC 3339 for python.
# Copyright (c) 2008, 2009, 2010 LShift Ltd. <query@lshift.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# SOURCE: https://github.com/tonyg/python-rfc3339/commit/61c4f7f7da270b754e7467c7633f6006e14fc828

import datetime, time, calendar
import re
#from datetime import tzinfo
from stix.utils import tzinfo


#__all__ = ["tzinfo", "UTC_TZ", "parse_date", "parse_datetime", "now", "utcfromtimestamp", "utctotimestamp", "datetimetostr", "timestamptostr", "strtotimestamp"]

ZERO = datetime.timedelta(0)
UTC_TZ = tzinfo(0, 'Z')

# date_re_str = r'(\d\d\d\d)-(\d\d)-(\d\d)'
# time_re_str = r'(\d\d):(\d\d):(\d\d)(\.(\d+))?([zZ]|(([-+])(\d\d):?(\d\d)))'
# date_re = re.compile(r'^\s*' + ''.join(date_re_str) + r'\s*$')
# datetime_re = re.compile(r'^\s*' + ''.join([date_re_str, "r'[ tT]'", time_re_str]) + r'\s*$')

# rfc3339_regex = re.compile(
#     r"^(\d\d\d\d)\-(\d\d)\-(\d\d)T"
#     r"(\d\d):(\d\d):(\d\d)(\.\d+)?(Z|([+\-])(\d\d):(\d\d))$")

rfc3339_regex = re.compile(
    r'(\d\d\d\d)-(\d\d)-(\d\d)'
    r'[ tT]'
    r'(\d\d):(\d\d):(\d\d)(\.(\d+))?([zZ]|(([-+])(\d\d):?(\d\d)))'
)


def main():

    print parse_datetime("2016-01-20T12:31:12.12345Z")
    print parse_datetime("2016-01-20T12:00:00Z")
    print parse_datetime("2016-01-20T12:00:00")
    print parse_datetime("2016-01-20 12:00:00+00:00")
    print parse_datetime("2016-01-20 12:00:00+23:59")
    print parse_datetime("2016-01-20 12:00:00-23:59")


def _offset_to_tzname(offset):
    offset = int(offset)
    if offset < 0:
        tzsign = '-'
    else:
        tzsign = '+'
    offset = abs(offset)
    tzhour = offset / 60
    tzmin = offset % 60
    return '%s%02d:%02d' % (tzsign, tzhour, tzmin)


def parse_datetime(s):
    print  s
    # match = datetime_re.match(s)
    match  = rfc3339_regex.match(s)
    if match:
        (y, m, d, hour, min, sec, ignore1, frac_sec, wholetz, ignore2, tzsign, tzhour, tzmin) = \
            match.groups()

        if frac_sec:
            frac_sec = float("0." + frac_sec)
        else:
            frac_sec = 0
        microsec = int((frac_sec * 1000000) + 0.5)

        if wholetz == 'z' or wholetz == 'Z':
            tz = UTC_TZ
        else:
            tzhour = int(tzhour)
            tzmin = int(tzmin)
            offset = tzhour * 60 + tzmin
            if offset == 0:
                tz = UTC_TZ
            else:
                if tzhour > 24 or tzmin > 60 or offset > 1439: ## see tzinfo docs for the 1439 part
                    raise ValueError('Invalid timezone offset', s, wholetz)

                if tzsign == '-':
                    offset = -offset
                tz = tzinfo(offset, _offset_to_tzname(offset))

        return datetime.datetime(int(y), int(m), int(d),
                                 int(hour), int(min), int(sec), microsec,
                                 tz)
    else:
        raise ValueError('Invalid RFC 3339 datetime string', s)


def now():
    """Return a timezone-aware datetime.datetime object in
    rfc3339.UTC_TZ timezone, representing the current moment
    (time.time()). Useful as a replacement for the (timezone-unaware)
    datetime.datetime.now() method."""
    return utcfromtimestamp(time.time())


def utcfromtimestamp(unix_epoch_timestamp):
    """Interprets its argument as a count of seconds elapsed since the
    Unix epoch, and returns a datetime.datetime in rfc3339.UTC_TZ
    timezone."""
    (y, m, d, hour, min, sec) = time.gmtime(unix_epoch_timestamp)[:6]
    return datetime.datetime(y, m, d, hour, min, sec, 0, UTC_TZ)


def utctotimestamp(dt):
    """Returns a count of the elapsed seconds between the Unix epoch
    and the passed-in datetime.datetime object."""
    return calendar.timegm(dt.utctimetuple())


def datetimetostr(dt):
    """Return a RFC3339 date-time string corresponding to the given
    datetime object."""
    if dt.utcoffset() is not None:
        return dt.isoformat()
    else:
        return "%sZ" % dt.isoformat()


def timestamptostr(ts):
    """Return a RFC3339 date-time string corresponding to the given
    Unix-epoch timestamp."""
    return datetimetostr(utcfromtimestamp(ts))


def strtotimestamp(s):
    """Return the Unix-epoch timestamp corresponding to the given RFC3339
    date-time string."""
    return utctotimestamp(parse_datetime(s))


# class tzinfo(datetime.tzinfo):
#     """
#     Implementation of a fixed-offset tzinfo.
#     """
#     def __init__(self, minutesEast = 0, name = 'Z'):
#         """
#         minutesEast -> number of minutes east of UTC that this tzinfo represents.
#         name -> symbolic (but uninterpreted) name of this tzinfo.
#         """
#         self.minutesEast = minutesEast
#         self.offset = datetime.timedelta(minutes = minutesEast)
#         self.name = name
#
#     def utcoffset(self, dt):
#         """Returns minutesEast from the constructor, as a datetime.timedelta."""
#         return self.offset
#
#     def dst(self, dt):
#         """This is a fixed offset tzinfo, so always returns a zero timedelta."""
#         return ZERO
#
#     def tzname(self, dt):
#         """Returns the name from the constructor."""
#         return self.name
#
#     def __repr__(self):
#         """If minutesEast==0, prints specially as rfc3339.UTC_TZ."""
#         if self.minutesEast == 0:
#             return "rfc3339.UTC_TZ"
#         else:
#             return "rfc3339.tzinfo(%s,%s)" % (self.minutesEast, repr(self.name))

if __name__ == '__main__':
    main()

# EOF
