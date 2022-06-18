# an exercise to use numbers and ranges of numbers

import math

print("Tell me a number please.")

num_1 = float(input("> "))

if num_1 > 0:
    print("This is a positive number,", end=' ')

    if num_1 in range(1,10):
        print("between 1 and 10")
    elif num_1 > 10:
        print("greater than 10")
    else:
        print("which is less than 1")
else:
    print("This is a negative number", end=' ')

    if num_1 in range(-10,-1):
        print("between -1 and -10")
    elif num_1<-10:
        print("less than -10")
    else:
        print("between -1 and 0")

#check if integer
if math.floor(num_1) == num_1:
    print("The number is an integer.")
else:
    print("The number is not an integer.")

abs_num_1 = math.sqrt(num_1*num_1)

print(f"The absolute value of the number is {abs_num_1}.")

num_2 = 3* (num_1 -1)

print(f"{num_2}")
