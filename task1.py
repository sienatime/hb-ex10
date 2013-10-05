#!/bin/env python

"""
Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""
l = [5,2,1,5,9,10,11]

for i in range(len(l)-1):
    tmp = l[i]

    print "comparing %d and %d" % (l[i], l[i+1])

    if l[i+1] < l[i]:
        l[i] = l[i+1]
        l[i+1] = tmp

    print l

l.reverse() # HAHA

print l, "final l"