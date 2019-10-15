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
print(archimedes(16))




#  see the lop above. in addition to the value of pi, print the difference
# between the values calculated by the archimedes function and by math.pi
# how many sides does it take to make the two close?


print(math.pi)



for sides in range(40000000, 400000000, 40000000):
    print(sides, archimedes(sides))

print(math.pi)

# there is no difference


# Accumalators

# not algebra; these are not equations

#accumalators can store value

# variable to handle the accumalation
acc = 0 #here is the original value of our accumalation
for val in range(1, 6, 1): #here is the parameters for our values
    acc = acc + val #here we add the values to our original accumalation

# the range is from and including the first number to but not including the next number
# the last number indicates by what interval you are jumping. We are jumping by 1 here
# take original value (0) and add a value (val) to it, all values from 1 to 6, and keep adding and storing in the accumalation
# 0+1=1, 1+2=3, 3+3=6, 6+4=10, 10+5=15

print(acc)

# we get 15

# here is the sum of the first 100 even numbers
acc = 0
for val in range(0, 201, 2):
    acc = acc + val

print(acc)


# sum of the first 50 odd numbers

acc = 0
for val in range(1, 101, 2):
    acc = acc + val

print(acc)


# average of the first 100 odd numbers

acc = 0




