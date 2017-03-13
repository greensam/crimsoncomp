#!/usr/bin/env python
import collections
import csv

def swapchars(s):

    counts = collections.Counter([c.lower() for c in s if c.isalpha()])

    most = max(counts, key=counts.get)
    least = min(counts, key=counts.get)

    def swap(c):

        if c.lower() == most:
            return least
        elif c.lower() == least:
            return most
        else:
            return c

    return "".join([swap(c) for c in s])

# assert swapchars("samuel lewis green") == "samual lawis graan"
print  swapchars('I\'m just a chi-town coder with a nice flow.') # == "U'm jist a chu-town coder wuth a nuce flow."


def sortcat(*arg):
    n = arg[0]
    strings = arg[1:]
    strings = sorted(strings, key=lambda l: len(l), reverse=True)

    if n == -1:
        return "".join(strings)
    else:
        return "".join(strings[:n])

assert sortcat(1, 'abc', 'bc') == 'abc'
assert sortcat(2, 'bc', 'c', 'abc') == 'abcbc'

def readdic():
    data = {}
    with open('states.txt') as f:
        reader = csv.reader(f)

        for state, abv in reader:
            data[abv] = state
    return data

DICT = readdic()

def bluesclues(abbv):
    
    return DICT[abbv]

def bluesbooze(state):
    rev = {state:abbv for abbv, state in DICT.iteritems()}
    return rev[state]

assert bluesclues('AL') == 'Alabama'
assert bluesclues('NY') == 'New York'
assert bluesbooze('New York') == 'NY'
assert bluesbooze('Connecticut') == 'CT'

