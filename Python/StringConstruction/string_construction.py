#!/bin/python
# https://www.hackerrank.com/challenges/string-construction

import sys

def stringConstruction(s):
    # Complete this function
    p = ""
    cost = 0

    for i in s:
        if i not in p:
            cost += 1
        p += i

    return cost

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = stringConstruction(s)
    print(result)
