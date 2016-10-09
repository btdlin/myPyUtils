#!/usr/bin/env python

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
print words[2]

# for loop example
fruit = "apple"
for letter in fruit:
    print letter


