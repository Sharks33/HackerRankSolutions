=begin
Dothraki are planning an attack to usurp King Robert's throne.
King Robert learns of this conspiracy from Raven and plans to
lock the single door through which the enemy can enter his kingdom.
But, to lock the door he needs a key that is an anagram of a certain
palindrome string. The king has a string composed of lowercase English
letters. Help him figure out whether any anagram of the string can be a
palindrome or not.

INPUT FORMAT
A single line which contains the input string.

CONSTRAINTS
1 <= length of string <= 10^5
Each character of the string is a lowercase English letter.

OUTPUT FORMAT
A single line which contains YES or NO in uppercase.

SAMPLE INPUT 0
aaabbbb

SAMPLE OUTPUT 0
YES

EXPLANATION 0
A palindrome permutation of the given string is bbaaabb.

SAMPLE INPUT 1
cdefghmnopqrstuvw

SAMPLE OUTPUT 1
NO

EXPLANATION 1
You can verify that the given string has no palindrome permutation.

SAMPLE INPUT 2
cdcdcdcdeeeef

SAMPLE OUTPUT 2
YES

EXPLANATION 2
A palindrome permutation of the given string is ddcceefeeccdd.
=end


#!/bin/ruby

def gameOfThrones(s)
    # Complete this function
    uniq_arr_s = s.split("").uniq
    print uniq_arr_s
end

s = gets.strip
result = gameOfThrones(s)
puts result;



