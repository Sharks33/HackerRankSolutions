# Alice is taking a cryptography class and finding anagrams to be very useful.
# We consider two strings to be anagrams of each other if the first string's
# letters can be rearranged to form the second string. In other words, both
# strings must contain the same exact letters in the same exact frequency For
# example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# Alice decides on an encryption scheme involving two large strings where
# encryption is dependent on the minimum number of character deletions required
# to make the two strings anagrams. Can you help her find this number?

# Given two strings, a and b, that may or may not be of the same length,
# determine the minimum number of character deletions required to make a
# and b anagrams. Any characters can be deleted from either of the strings.

# The first line contains a single string, a.
# The second line contains a single string, b.

# CONSTRAINTS
# 1 <= |a|, |b| <= 10^4
# It is guaranteed that a and b consist of lowercase English letters.

# OUTPUT FORMAT
# Print a single integer denoting the number of characters which must be
# deleted to make the two strings anagrams of each other.

# SAMPLE INPUT
# cde
# abc

# SAMPLE OUTPUT
# 4

# EXPLANATION
# We delete the following characters from our two strings to turn them into
# anagrams of each other:

# Remove d and e from cde to get c.
# Remove a and b from abc to get c.
# We had to delete 4 characters to make both strings anagrams, so we print 4
# on a new line.



#!/bin/python

def makingAnagrams(s1, s2)
    # Complete this function
    count = 0
    s1_uniq_arr = s1.split("").uniq
    s2_uniq_arr = s2.split("").uniq

    for i in s1_uniq_arr
        if s1.count(i) > s2.count(i)
            count += (s1.count(i) - s2.count(i)).abs
        end
    end

    for i in s2_uniq_arr
        if s2.count(i) > s1.count(i)
            count += (s2.count(i) - s1.count(i)).abs
        end
    end

    return count
end

s1 = gets.strip
s2 = gets.strip
result = makingAnagrams(s1, s2)
puts result;


