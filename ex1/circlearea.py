#!/usr/bin/env python
import math

rad = int(input("Enter the desired radius: "))

totalcirclearea = math.pi * math.pow (rad, 2)

#This statement rounds up the total area calculated to 2 decimal point
#Uncomment it by removing the "#" in front of the statement below to see the magic
#totalcirclearea = format(totalcirclearea,'.2f')

print ("The area of the circle is therefore: " + str(totalcirclearea) + ".")