#!/usr/bin/env python
import math

rad = input("Enter the desired radius: ")

spherevolume = (4/3) * math.pi * math.pow (rad, 2)

#This statement rounds up the total area calculated to 2 decimal point
#Uncomment it to see the magic
#spherevolume = format(spherevolume,'.2f')

print "The volume of the sphere is therefore: " , str(spherevolume) , "."