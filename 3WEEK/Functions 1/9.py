from cmath import pi


import math
def volume(r):
    return 4/3*pi*r**3
r=int(input("Enter the radius of sphere:\n"))
print("The volume of sphere is "+str(volume(r)))