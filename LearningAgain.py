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

# Compute the sum of the first 100 even numbers             10100

# Compute the sum of the first 50 odd numbers               2500

# Compute the average of the first 100 odd numbers          100

# Write a function that returns the average of the first N numbers, where
#   N is a parameter                                        N = 6, average = 21

# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter                         N = 6, factorial = 720

# Each number in the Fibonacci sequence is the sum of the previous two numbers.
#   The first two numbers in the sequence are 1 and 1.  Compute the 10th
#   Fibonacci number.                                       The 10th Fibonacci number is 55

# Write a function to compute the Nth Fibonacci number, where N is a parameter.
#   You may assume that N will be greater than or equal to 3.



# here is the sum of the first 100 even numbers
acc = 0
for val in range(0, 201, 2):
    acc = acc + val

print(acc)

# it is 10100


# sum of the first 50 odd numbers

acc = 0
for val in range(1, 100, 2):
    acc = acc + val

print(acc)

# it is 2500


# average of the first 100 odd numbers

acc = 0
for val in range(1, 200, 2):
    acc = acc + val / 100

print(acc)

# it is 100

# function for the average of N numbers where N is a parameter

def average(N):
    acc = 0
    for average in range(0, 37, N):
        acc = acc + average
    print(acc/N)

print(average(6))

# N = 6, average = 21

# this is function finds the product of N numbers, where N is a parameter
def factorial(N):
    acc = 1
    for factorial in range(1, N+1, 1):
        acc = acc * factorial
    print(acc)


print(factorial(6))

# N = 6, Factorial  = 720


# this calculates the 10th fibonacci number

acc = 0
for fibonacci in range(1, 11):
    acc = acc + fibonacci
    print(acc)

# it is 55


# this computes the Nth fibonacci number where n is a parameter
def Fibonacci(N):
    acc = 0
    for fibonacci in range(1, N+1):
        acc = acc + fibonacci
    print(acc)


print(Fibonacci(10))

# the variable is 10, the answer is 55

# a Monte Carlo Simulation
# randomization
# random numbers

import random

print(random.random())

# 0<=x<1

# Boolean Expressions
# compares two things
# built using <, <=, >, >=, ==, !=

# Compound Boolean Expressions
# uses and, or, not

dogWeight = 25

print(dogWeight < 25)

# see we can see if certain comparisons are true or false

catWeight = 12
print(dogWeight >= 25 or catWeight <= 12)
# and requires both to be true, or only needs one
print(not catWeight <=10)
# not flips the true/false value

# decision making skills

jon = 20
lyndsi = 15
andrew = 25
ans = 0

if jon > 20:
    if lyndsi < 50:
        ans = 42069
    else:
        ans = 200

else:
    if andrew > 500:
        ans = 150
    else:
        ans = 75
print(ans)





value = 75
if value > 100:
    print("bigger than 100")
elif value > 80:
    print("bigger than 80")
elif value > 45:
    print("bigger than 45")
else:
    print("not bigger than much")


def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi

print(montePi(1000))




import turtle


def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()
  

    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()



    inCircle = 0
    t.penup

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)
        t.goto(x, y)
        t.goto(-x, y)
        t.goto(-x, -y)
        t.goto(x, -y)

        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else:
            t.color("red")

        t.dot()

    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi

print(showMontePi(1000))

#assigment: modify the code to plot points in the entire circle(all four quadrants)
# you will have to adjust the calculated value for pi accordingly

















