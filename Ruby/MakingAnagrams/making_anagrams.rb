#!/bin/python
# https://www.hackerrank.com/challenges/making-anagrams

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


