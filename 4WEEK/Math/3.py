import math
n=int(input('number of sides:'))
a=int(input('length of a side:'))
print((n*(a**2))/4*math.tan(math.radians(180/n)))
