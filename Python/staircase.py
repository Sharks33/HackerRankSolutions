'''
Consider a staircase of size n = 4:

   #
  ##
 ###
####

Observe that its base and height are both equal to n, and the image is drawn
using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.

INPUT FORMAT
A single integer, n, denoting the size of the staircase.

OUTPUT FORMAT
Print a staircase of size n using # symbols and spaces.

Note: The last line must have 0 spaces in it.

SAMPLE INPUT
6

SAMPLE OUTPUT

     #
    ##
   ###
  ####
 #####
######

EXPLANATION
The staircase is right-aligned, composed of # symbols and spaces, and has a
height and width of n = 6.
'''

#!/bin/python

import sys

n = int(raw_input().strip())

space = ''
pound = ''
for i in xrange(n):
    n = n - 1
    space = ' ' * n
    pound += '#'
    print space + pound
