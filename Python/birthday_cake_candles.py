'''
Colleen is turning n years old! Therefore, she has n candles of various heights on her cake,
and candle i has height h. Because the taller candles tower over the shorter ones, Colleen
can only blow out the tallest candles.

Given the h for each individual candle, find and print the number of candles she can
successfully blow out.

INPUT FORMAT
The first line contains a single integer, n, denoting the number of candles on the cake.
The second line contains n space-separated integers, where each integer  describes the
height of candle i.

CONSTRAINTS
1 <= n <= 10^5
1 <= h <= 10^7

OUTPUT FORMAT
Print the number of candles Colleen blows out on a new line.

SAMPLE INPUT 0
4
3 2 1 3

SAMPLE OUTPUT 0
2

EXPLANATION 0
We have one candle of height 1, one candle of height 2, and two candles of height 3.
Colleen only blows out the tallest candles, meaning the candles where h = 3. Because
there are  such candles, we print 2 on a new line.
'''


#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    max_val = max(i for i in ar)
    max_val_occ = ar.count(max_val)
    return max_val_occ

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
