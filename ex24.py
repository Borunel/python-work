print("Let's practice everything!")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')
#the following is a spanning string inside """ set to the variable poem
poem = """
\t The lovely World
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem) # print variable poem
print("--------------")


five =10 - 2 + 3 - 6 # five is declared as the arithmetic Here
print(f"This should be five: {five}") # use of fast string to insert variable five into string

def secret_formula(started): # function takes argument 'started' and returns three variables after arithmetic on 'started'
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point =  10000 # start point is 10000
beans, jars, crates = secret_formula(start_point) # declares 3 variables which are returned in that order when function is called

# remember this is another way to format a string..
print("With a starting point of {}".format(start_point)) # print a string with empty variable - which is then formatted with variable start_point --- note f -string not used!!!
#its just like with an f-string
print(f"We'd have {beans} beans, {jars} jars and {crates} crates.") # then uses f-string

start_point = start_point / 10 # new start point

print("We can also do that this way:")
formula = secret_formula(start_point) #formula is now result of calling functions
#this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars and {} crates".format(*formula)) # empty variables formatted with format() note *formula in function..
# if we only asked for formula and formatted it into a single empty holder it would return <500000.0, 500.0, 5.0> i.e all three values in bra-ket
