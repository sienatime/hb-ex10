#!/bin/env python

"""
Write a function with the following signature:
    title(str) -> str

It should take a string and capitalize it according to book title rules
    eg:
    title("a tale of two cities")
        => A Tale of Two Cities
"""

def title(my_title):
    #always capitalize first and last words
    #don't capitalize articles and prepositions fewer than 3 letters
    ignore = parse()
    new_title = ""
    tokens = my_title.split()

    for i in range(len(tokens)):
        if tokens[i].lower() not in ignore or i == 0 or i == len(tokens)-1:
            new_title += tokens[i].title()
        else:
            new_title += tokens[i].lower()

        if i < len(tokens):
            new_title += " "

    return new_title

def parse():
    f = open("prepositions.txt")
    lines = f.readlines()
    f.close()

    short_words = []

    for line in lines:
        if len(line.strip("\n")) <= 4:
            short_words.append(line.strip("\n"))

    return short_words

print title("WAR AND PEACE")
print title("a tale of two cities")
print title("of mice and men")
print title("the catcher in the rye")