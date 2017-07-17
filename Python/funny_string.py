'''
Suppose you have a String, S, of length N that is indexed from 0 to N - 1.
You also have some String, R, that is the reverse of String S. S is funny if
the condition |S[i] - S[i - 1]| = |R[i] - R[i - 1]| is true for every character i
from 1 to N - 1.

Note: For some String S, S[i] denotes the ASCII value of the i^th 0-indexed character in S.
The absolute value of an integer, x, is written as |x|.

INPUT FORMAT
The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a string, S.

CONSTRAINTS
1 <= T <= 10
0 <= i <= T - 1
2 <= length of S <= 10000

OUTPUT FORMAT
For each String S_j (where 0 <= j <= T - 1), print whether it is FUNNY or NOT FUNNY on a new line.

SAMPLE INPUT
2
acxz
bcxz

SAMPLE OUTPUT
Funny
Not Funny

EXPLANATION
Test Case 0: S = "acxz"
|c - a| = 2 = |x - z|
|x - c| = 21 = |c - x|
|z - x| = 2 = |a - c|
As each comparison is equal, we print Funny.

Test Case 1:  S = "bcxz"
|c - b| = 1, but |x - z| = 2
At this point, we stop evaluating S (as |c - b| != |x - z|) and print Not Funny.
'''



#!/bin/python

import sys

def funnyString(s):
    # Complete this function
    lst_1 = []
    lst_2 = []

    for i in s:
        lst_1 += i

    for j in lst_1:
        ascii_val = ord(j)
        lst_2.insert(0, ascii_val)

    reverse_lst_2 = list(reversed(lst_2))
    funny_str = ""

    for k, (val_1, val_2) in enumerate(zip(lst_2, reverse_lst_2)):
        if abs(lst_2[k] - lst_2[k-1]) != abs(reverse_lst_2[k] - reverse_lst_2[k-1]):
            funny_str = "Not Funny"
            break
        else:
            funny_str = "Funny"

    return funny_str



q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = funnyString(s)
    print(result)



