###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = float(input(""))
b = float(input(""))
c = float(input(""))
volume_cuboid = a * b * c
surface_area = 2 * (a*b + b*c + a*c)

print(volume_cuboid)
print(surface_area)