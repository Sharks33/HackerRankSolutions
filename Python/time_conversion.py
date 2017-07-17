'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

INPUT FORMAT
A single string containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM),
where 01 <= hh <= 12 and 00 <= mm,ss <= 59.

OUTPUT FORMAT
Convert and print the given time in 24-hour format, where 01 <= hh <= 23.

SAMPLE INPUT
07:05:45PM

SAMPLE OUTPUT
19:05:45
'''


#!/bin/python

import sys

def timeConversion(s):
    # Complete this function
    # OMG this is just ugly, code needs Refactor at later date
    if "PM" in s:
        mil_time = s.replace("PM","")
        conversion_int = int(mil_time[:2])
        if conversion_int != 12:
            conversion_int += 12
        elif conversion_int > 23:
            conversion_int = str("00")
        conversion_str = str(conversion_int)
        mil_time = mil_time.replace(mil_time[:2], conversion_str, 1)
        return mil_time
    else:
        mil_time = s.replace("AM","")
        conversion_int = int(mil_time[:2])
        if conversion_int > 11:
            conversion_int = str("00")
        elif conversion_int < 10:
            conversion_int = "0" + str(conversion_int)
        conversion_str = str(conversion_int)
        mil_time = mil_time.replace(mil_time[:2], conversion_str, 1)
        return mil_time

s = raw_input().strip()
result = timeConversion(s)
print(result)
