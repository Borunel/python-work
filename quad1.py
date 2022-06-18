from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import math

def add(x, y): # define function add with arguments x and y
    #print(f"ADDING {x} + {y}") # info line
    return x + y # function return x + y

def subtract(x, y): # define function subtract with arguments x and y again
    #print(f"SUBTRACTING {x} - {y}") # info line
    return x - y # function returns x + y

def multiply(x, y): # define function multiply with arguments x and y
    #print(f"MULTIPLYING {x} * {y}") # info line
    return x * y # returns x * y

def divide(x, y): # define function divide with arguments x and y
    #print(f"DIVIDING {x} / {y}") # info line
    return x / y # function returns x / y

def exponential(x, y): #define function to raise x to power of y
    return x ** y # function returns x**y

def x_find(): # function to define the left and right linits of the final plot
    if discr < 0:
        left_r, right_r = complex(real_part)
    elif discr > 0:
        left_r, right_r = two_root(root_1, root_2)
    elif discr == 0:
        left_r, right_r = rep_root(root_0)
    return left_r, right_r

def two_root(r_1, r_2): # limits if two roots and real
    if r_1 < r_2: # is r_1 to the left?
        left_r = r_1 - 2
        right_r = r_2 + 2
        return left_r, right_r
    elif r_1 > r_2: # or to the right?
        left_r = r_2 - 2
        right_r = r_1 + 2
        return left_r, right_r


def rep_root(r_0): # limits if one root repeated
    left_r = r_0 - 4
    right_r = r_0 + 4
    return left_r, right_r


def complex(real_part): #limits if complex roots
    left_r = real_part - 4
    right_r = real_part + 4
    return left_r, right_r


def max_turn(y_max): # subroutine if turning point is max

    if y_max > 0:
        y_top = y_max + 1
        y_bot = -10
    elif y_top == 0:
        y_top = 2
        y_bot = -10
    else:
        y_top = y_max + 10
        y_bottom = y_max -10
    return y_bot, y_top

def min_turn(y_min): # subroutine if turing point is minimum

    if y_min > 0:
        y_bot = y_min - 2
        y_top = 10
    elif y_min == 0:
        y_bot = -2
        y_top = 10
    else:
        y_bot = y_min - 2
        y_top = 2
    return y_bot, y_top

def y_find():
    if maximum == True:
        y_bottom, y_top = max_turn(y_0)
    else:
        y_bottom, y_top = min_turn(y_0)
    return y_bottom, y_top

def x_limiter(x_0, x_n):
    x_left = x_0 - (10 * x_0)
    x_right = x_n + (10 * x_0)
    return x_left, x_right


# body

print("For a quadratic equation of the form ax\u00B2 + bx + c we can find the roots if they exist.")
print("What is a? ")
a = float(input("> "))

print("what is b? ")
b = float(input("> "))

print("What is c? ")
c = float(input("> "))

#check entries
if a == 0:
    print("Equation is not quadratic.")
    exit(0)

discr = subtract(multiply(b,b),multiply(4, multiply(a, c)))
# check discriminant
if discr == 0:
    print("Two equal real roots")
    root_0 = divide(-b, multiply(2, a))
    print(f"Root is {root_0} repeated.")

elif discr > 0:
    print("Two real roots")
    root_1 = divide(add(-b, sqrt(discr)),multiply(2, a))
    root_2 = divide(subtract(-b, sqrt(discr)),multiply(2, a))
    print(f"Roots are: {root_1} and {root_2}")

else:
    print("Imaginary roots")
    real_part = divide(-b, multiply(2, a)) # -b/2a
    imaginary_part = round((divide(sqrt(sqrt(multiply(discr,discr))),multiply(2, a))),2) #square root of absolute value
    print(f"Roots are {real_part}+i{imaginary_part} and\n {real_part}-i{imaginary_part}")

if a == 1:
    ae = ''

else:
    ae = a

original_equation = f"y = {ae}x\u00B2 + {b}x + {c}"

print(original_equation)

    #differentiate
    #dy/dx = 2ax+b = 0
    #x = -b/2a
x_0 = -b/(2*a)
y_0 = a * (x_0 ** 2) + (b * x_0) + c
# 2nd derivative d2y/dx2 = 2a
#if 2a +ve then minumum else maximum
if (2 * a) < 0:
    turn = 'Maximum'
    maximum = True
else:
    turn = 'Minimum'
    maximum = False

print(f"{turn} turning point at {y_0},{x_0}")

left_r, right_r = x_find() # allocate left and right limits using x_find function
y_bottom, y_top = y_find()

x_0, x_n = x_limiter(left_r, right_r)

abs_x = sqrt(x_0 * x_0)
abs_xn = sqrt(x_n * x_n)

range = int((abs_x+ abs_xn)*10)

x = np.linspace(x_0, x_n, range ) # x axis values
y = (a* (x * x) + (b * x) + c)

fig = plt.figure()
fig.suptitle('Quadratic Solver')

ax = fig.add_subplot(111)


#print(f" left limit is {left_r}, right limit is {right_r}")
#print(f" top limit is {y_top}, bottom limit is {y_bottom}")
plt.ylim(y_bottom, y_top)



plt.xlim(left_r, right_r) # sets the limits on the x axis per left and right

ax.spines['left'].set_position('zero') # sets the left spine (axis) at zero
ax.spines['right'].set_color('none') # sets the right axis to be invisible - ie there is no right edge to the box
ax.spines['bottom'].set_position('zero') # bottom spine becomes the x axis
ax.spines['top'].set_color('none') # top spine is invisible.

# plotting the points
plt.plot(x, y)

# naming the x axis
#plt.xlabel('x - axis')
# naming the y axis
#plt.ylabel('y - axis')

# giving a title to my graph
plt.title(f"Plot of {original_equation}")

# function to show the plot
plt.show()
