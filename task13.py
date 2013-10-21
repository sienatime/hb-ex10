'''

'''
import math

def round(decimal):
    base = int(decimal)
    if decimal - base >= 0.5:
        return base+1
    else:
        return base
    
def count_lines(lines):
    if not lines:
        return 0
    count = 1
    for character in lines:
        if character == "\n":
           count  += 1    
    return count

def get_hypotenuse(side1, side2):
    hypotenuse = side1 * side1 + side2 * side2
    return math.sqrt(hypotenuse)
    

def reverse_list(l):
    size = len(l)
    for i in range(len(l)/2):
        temp = l[i]
        l[i] = l[size-i-1]
        l[size-i-1] = temp
        
    return l
    
def count_letters():
    inp = open("sample_input.txt")
    lines = inp.read()
    letters = lines.split()
    letter_count = dict()
    for letter in letters:
        existing_count = letter_count.get(letter, 0)
        existing_count += 1
        letter_count[letter] = existing_count
    
    for letter, count in letter_count.iteritems():
        print "%s:\t%d"%(letter, count)

def bubble_sort(l):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                tmp = l[i]
                l[i] = l[i+1]
                l[i+1] = tmp
                swapped = True

    return l
