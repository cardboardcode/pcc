#!/usr/bin/env python

_daword = raw_input("Input the word: ")

index = input("Input the index:  ")

if (index >= len(_daword)):
	print("Index Out Of Bounds")
else:
	print "The letter you want is: " , _daword[index] , "."
