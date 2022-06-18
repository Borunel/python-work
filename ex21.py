def add(a, b): # define function add with arguments a and b
    print(f"ADDING {a} + {b}") # info line
    return a + b # function return a+b

def subtract(a, b): # define function subtract with arguments a and b again
    print(f"SUBTRACTING {a} - {b}") # info line
    return a - b # function returns a + b

def multiply(a, b): # define function multiply with arguments a and b
    print(f"MULTIPLYING {a} * {b}") # info line
    return a * b # returns a * b

def divide(a, b): # define function divide with arguments a and b
    print(f"DIVIDING {a} / {b}") # info line
    return a / b # function returns a / b


print("Let's do some maths with just functions!!!1") # prints info

age = add(40, 7) #declares variable age to be the result of calling function add with arguments 40 and 7
height = subtract(200, 4)# declares the variable height to be the result of calling function subtract with arguments 200 and 4
weight = multiply(50, 2) # declares the variable weight to be the result of calling function multiply with arguments 50 and 2
iq = divide(100, 2) # declares the variable iq to be the result of calling function divide with arguments 100 and 2

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}") #prints out the values of age, height, weight and iq


# A puzzle for the extra credit, type it in anyway.
print("Here is the puzzle.") # info line

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # compound equation works from innermost function outwards - not bidmas

print("That becomes: ", what, "Can you do it by hand?") # why yes, yes I can...
