#!/bin/env python

"""
Given the list l composed of tuples, sort the list by the second item in the tuple
    l = [(1,3), (3,2), (5,1)]
    becomes
    l = [(5,1), (3,2), (1,3)]

"""

l = [(1,2), (3,1), (17, 35), (81,20), (1,2)]

# what is it, compare two things and if they are smaller, swap them?
swapped = True
j = 0

while swapped:
    swapped = False
    j += 1
    for i in range(len(l)-j):
        tmp = l[i]

        if l[i+1][1] < l[i][1]:
            l[i] = l[i+1]
            l[i+1] = tmp
            swapped = True

print l