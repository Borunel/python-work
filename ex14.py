from sys import argv #initial set up import argv stuff?

script, user_name, age = argv #two modules script name and user_name so expects one command line  switch
prompt = '>' # declares a variable prompt which is a greater than sign

print(f"Hi {user_name} who is {age} years old, I'm the {script} script.") # prints an f-string which tells you the initial argv info
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?") # asks a question including argv
likes = input(prompt) # requests input from the user with a 'placeholder' of prompt allocates it to the variable likes

print(f"Where do you live {user_name}?") # asks where you live
lives = input(prompt) # requests data from user and allocates it to a variable

print("What type of computer do you have?") # asks what sort of computer you have
computer = input(prompt) # requests data and allocates it to variable

print(f"Tell me a number {user_name}")
number = int(input(prompt))

print(f"""
    Alright, so you said {likes} about liking me.
    And you live in {lives}. Not sure where that is.
    And you have a {computer} computer.
    You gave me {number} as a free gift. I hate it.
    """) # outputs the data provided with narrative
