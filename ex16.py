from sys import argv # uses the command line argument which is provided on running

script, filename = argv #allocates the variables to the arguments

print(f"We're going to erase {filename}.") # tells us what its going to do using an f-string
print("If you don't want that, hit CTRL-C (^C).") # tells you how to interrupt and stop the programme if you don't want it to happens
print("If you do want that, hit RETURN.") # tells you what to do to continue

input("?") # requests an input from the user ctrl-c automatically breaks the programme , return automatically allows it to continue

print("Opening the file...") #info
target = open(filename, 'w') # opens given argv filename with switch w (writeable?)

print("Truncating the file. Goodbye!") # info
target.truncate() #runs operation truncate on the file (truncates to zero in this case?)

print("Now, I'm going to ask you for three lines.") # info

line1 = input("line 1: ") # allocates first input to line1
line2 = input("line 2: ") # allocates first input to line2
line3 = input("line 3: ") # allocates first input to line3

print("I'm going to write these to the file.") #info

target.write(line1) # writes line1 to given file
target.write("\n") # adds a newline to file
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()

target2 = open(filename)

print("It now looks like this: \n", target2.read())

print("And finally we close it.")
target.close() # closes file for completeness
