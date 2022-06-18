types_of_people = 10 # Set variable(?) as named at 10
x = f"There are {types_of_people} types of people." # f-string established in variable x with the variable in line 1 embedded

binary = "binary" # allocate a string to a variable
do_not = "don't" # allocate a string to a variable
y=f"Those who know {binary} and those who {do_not}." #f-string established with previous two variables embedded - allocated to variable y

print(x) # print f-string in x
print(y) # print f-string in y

print(f"I said: {x}") # print a new f-string with the f-string in x nested within
print(f"I also said: '{y}'") # print a new f-string with the f-string in y nested within

hilarious = False # telling us that the variable hilarious is false with the 'False' boolean value
joke_evaluation = "Isn't that joke so funny?! {}" # a named variable with an anonymous embed?

print(joke_evaluation.format(hilarious)) # print the expression in 15 and insert the boolean from 14

w = "This is the left side of..." # establish a variable with a string
e = "a string with a right side." # establish another variable with a string

print(w + e) # print the two variables (strings) together with each other
