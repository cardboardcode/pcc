#!/usr/bin/env python
import math

rad = input("Enter the desired radius: ")

totalcirclearea = math.pi * math.pow (rad, 2)

#This statement rounds up the total area calculated to 2 decimal point
#Uncomment it to see the magic
#totalcirclearea = format(totalcirclearea,'.2f')

print "The area of the circle is therefore: " , str(totalcirclearea) , "."