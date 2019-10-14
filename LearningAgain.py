# we are looking at approximations of pi
# as well as looking at the math Module

print(22/7)
print(355/113)

import math

print(9801 / (2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(4))
print(archimedes(8))
print(archimedes(360000000))




#  see the lop above. in addition to the value of pi, print the difference
# between the values calculated by the archimedes function and by math.pi
# how many sides does it take to make the two close?


print(math.pi)

# it takes 360 million sides to make the archimedes function equal to math.pi
# the difference is 0 because they are now equal
