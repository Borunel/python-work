print("How old are you?", end = ' ') # end = ' ' tells python not to end the line with a newline
age = input() #input() takes a string and records it to the declared variable
print("How tall are you?", end = ' ') # because left to its own devices it does that automatically
height = input()
print("How much do you weigh?", end =' ')
weight = input()

print(f"So you're {age} years old, {height} cm tall and {weight} kg in weight.") # f-string inserts the named variables into the printed output.
