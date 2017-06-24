#!/usr/bin/env python

_daword = input("Input the word: ")

index = int(input("Input the index:  "))

if (index >= len(_daword)):
	print("Index Out Of Bounds")
else:
	print ("The letter you want is: " + _daword[index] + ".")
