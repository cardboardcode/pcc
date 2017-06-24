#!/usr/bin/env python

_daword = input("Input the word: ")

# Finding the number of 'a' characters in the string you input
count = _daword.count('a', 0, len(_daword) )

print ("Your string contains " + str(count) + " occurences of 'a'.")
