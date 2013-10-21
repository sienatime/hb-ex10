#!/bin/env python

"""
Write the following two functions
    c_to_f(float) -> float
    f_to_c(float) -> float

c_to_f should convert a temperature in celsius to fahrenheit, and f_to_c should do the opposite
"""

def c_to_f(temp):
    return temp * 9/5.0 + 32

def f_to_c(temp):
    return (temp - 32) * 5/9.0

print f_to_c(100)
print c_to_f(0)