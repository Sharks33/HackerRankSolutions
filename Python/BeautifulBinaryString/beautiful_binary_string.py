#!/bin/python

import sys

def minSteps(n, B):
    # Complete this function
    num_occ = B.count("010")
    return num_occ

n = int(raw_input().strip())
B = raw_input().strip()
result = minSteps(n, B)
print(result)
