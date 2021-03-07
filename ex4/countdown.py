#!/usr/bin/env python

print ("Input number of iterations you wish to make: ")
iterations = int(input()) 

for index in range(iterations + 1):
	print ("Counting down... " + str(iterations - index))
	index += 1 