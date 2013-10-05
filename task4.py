#!/bin/env python

"""
Given the string s, split it into two strings, s2 and s3, s2 containing the first 5 letters of the string, and s3 containing the remaining letters.

eg:
    s1 = "Hello there"
    s2 = "Hello"
    s3 = " there"

"""
s = "Hi there, my name is Slim"

s1 = s[:6]
s2 = s[6:]

print s1
print s2