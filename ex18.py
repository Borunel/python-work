# This is like your scripts with argv
#lines 3 to 5 all define the function print_two, hence the indent
def print_two(*args): #defines a function called print_two which takes -all- the arguments of args
    arg1, arg2 = args #declares args to consist of arg1 and arg2 in that order
    print(f"arg1: {arg1}, arg2: {arg2}") #prints arg1 and arg2 with label strings

# okay, that args is totally pointless, we can just do this:
def print_two_again(arg1, arg2): # defines the same function with a different label but which directly takes arg1 and arg2
    print(f"arg1: {arg1}, arg2: {arg2}") #prints arg1 and arg2 with label strings

# THis takes just one arguments
def print_one(arg1): #defines a function called print_one which takes a single argument arg1
    print(f"arg1: {arg1}") # prints arg1 with label string

# This one takes no argumnents
def print_none(): #defines a function print_none which doesn't take any arguments
    print("Nothin to print. Except this.") #informs that this function has nothing to print as it has no arguments

print_two("John","Moran") #call funtion print_two with arg1 as John and arg2 as Moran
print_two_again("John","Moran") # call print_two_funtion again with arg1 as John and arg2 as Moran
print_one("One") # call print_one function with arg1 as one
print_none() # call print_none function with no arguments expected
#if you give the wrong number of arguments it will give an error and tell you that x number of arguments expected but y arguments given.

craps1 = input("What is the first type of garbage? ")
craps2 = input("What is the second type of garbage? ")
craps3 = input("What is the last type of garbage? ")

def print_garbage(crap1, crap2, crap3):
    print(f"This place is full of {crap1}, {crap2} and loads of {crap3}")

print_garbage(craps1, craps2, craps3)
