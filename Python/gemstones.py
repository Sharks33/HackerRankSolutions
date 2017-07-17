'''
John has discovered various rocks. Each rock is composed of various elements,
and each element is represented by a lower-case Latin letter from 'a' to 'z'.
An element can be present multiple times in a rock. An element is called a
gem-element if it occurs at least once in each of the rocks.

Given the list of N rocks with their compositions, display the number of
gem-elements that exist in those rocks.

INPUT FORMAT
The first line consists of an integer, N, the number of rocks.
Each of the next N lines contains a rock's composition. Each composition
consists of lower-case letters of English alphabet.

CONSTRAINTS
1 <= N <= 100
Each composition consists of only lower-case Latin letters ('a'-'z').
1 <= length of each composition <=100

OUTPUT FORMAT
Print the number of gem-elements that are common in these rocks. If there are none,
print 0.

SAMPLE INPUT
3
abcdde
baccd
eeabg

SAMPLE OUTPUT
2

EXPLANATION
Only "a" and "b" are the two kinds of gem-elements, since these are the only
characters that occur in every rock's composition.
'''


import sys

def gemstones(arr):
    # Complete this function
    first_sample = list(arr[0])
    gem_total = 0
    # matching = [s for s in first_sample if first_sample.strip() in all(s)]
    for i in arr:
        print "test loop 1: i = ", i
        gem = 0
        sample = list(i)
        for j in sample:
            print j
            print "test loop 2"
            if j not in first_sample:
                print "test if 3"
                break
            else:
                print "test else 4"
                gem += 1
                if gem == n:
                    print "test if 5"
                    gem_total += 1
                    first_sample.pop(0)

        gemstones(first_sample)
    return gem_total
        # if sample not in first_sample:
        #     print "flase"
        #     break
        # else:
            # print "true"
        # print sample
    #     matching = [s for s in arr if first_sample in all(s)]
    #     print matching
        # if any(first_sample in s for s in arr):
        #     print "true"
        # else:
        #     print"false"
        # print i
        # if any((c in first_sample) for c in arr[i]):
        #     print "TRUE"
        # else:
        #     print "FALSE"
        # print arr

n = int(raw_input().strip())
arr = []
arr_i = 0
for arr_i in xrange(n):
    arr_t = str(raw_input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)
