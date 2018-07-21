#!/bin/ruby

def stringConstruction(s)
    # Complete this function
    p_str = ""
    cost = 0

    s.split("").each do |i|
        if !p_str.include? i
           cost += 1
        end
        p_str += i
    end

    return cost
end

q = gets.strip.to_i
for a0 in (0..q-1)
    s = gets.strip
    result = stringConstruction(s)
    puts result;
end
