#!/bin/env python

"""
Given list l1 and list l2, produce list l3 that contains the contents of both lists, removing duplicates
eg:
    l1 = [1,2,3]
    l2 = [2,3,4]
    
    l3 = [1,2,3,4]
"""
l1 = [1, 3, 4, 6, 8, 4, 10]
l2 = [93, 2, 23, 77, 66, 3]

l3 = []

both_lists = l1 + l2

for item in both_lists:
    if item not in l3:
        l3.append(item)

print l3