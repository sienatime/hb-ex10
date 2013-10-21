#!/bin/env python

"""
Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""
l = [5,2,1,5,9,10,11]

swapped = True
j = 0

while swapped:
    swapped = False
    j += 1
    for i in range(len(l)-j):
        tmp = l[i]

        print "comparing %d and %d" % (l[i], l[i+1])

        if l[i+1] > l[i]:
            l[i] = l[i+1]
            l[i+1] = tmp
            swapped = True

    print l

#l.reverse() # HAHA

print l, "final l"