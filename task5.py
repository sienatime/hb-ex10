#!/bin/env python

"""
Given the string s, excise characters 6 through 12, inclusive 
eg:
    s = "Hello, good sir"
    becomes 
    s = "Hello sir"

    this is not inclusive? this 6 is included but 12 is not. the 12th character is the space between good and sir but there is a space in the above answer.
"""
s = "Hi there, my name is Slim"

# the 6th character is at index 5 and the 12th character is at index 11.
s1 = s[:5] # up to but not including index 5 (6th element)
s2 = s[11:] # from index 11 (12th element) to the end

s = s[:5] + s[11:]

print s