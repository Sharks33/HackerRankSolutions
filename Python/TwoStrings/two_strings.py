#!/bin/python

import sys

def twoStrings(s1, s2):
    # Complete this function
    s1_set = set(s1)
    s2_set = set(s2)
    has_sub_str = "NO"

    for i in s1:
        if i in s2_set:
            has_sub_str = "YES"

    for i in s2:
        if i in s1_set:
            has_sub_str = "YES"

    return has_sub_str

q = int(raw_input().strip())
for a0 in xrange(q):
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    result = twoStrings(s1, s2)
    print(result)
