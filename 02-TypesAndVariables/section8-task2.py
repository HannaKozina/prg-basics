###
# Calculation of circle area and circumference
#

# determine radius and PI values
# calculate area
# calculate circumference
# print results
import math

radius = float(input("Enter radius : "))
area = math.pi * radius**2
circumference = 2 * math.pi * radius
area = round(area, 2)
circumference = round(circumference, 2)
print( area, circumference)
