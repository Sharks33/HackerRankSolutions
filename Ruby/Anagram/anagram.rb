#!/bin/ruby
# https://www.hackerrank.com/challenges/anagram

def anagram(s)
    # Complete this function
    if s.length % 2 != 0
        return -1
    else
        count = 0
        str_1 = s.slice(0..(s.length / 2) - 1)
        str_2 = s.slice(s.length / 2..-1)
        arr_s = s.split("").uniq

        for i in arr_s
            str_1_count = str_1.count(i)
            str_2_count = str_2.count(i)

            if str_1_count != str_2_count
                count += (str_1_count - str_2_count).abs
            end
        end

        return count / 2
    end
end

q = gets.strip.to_i
for a0 in (0..q-1)
    s = gets.strip
    result = anagram(s)
    puts result;
end
