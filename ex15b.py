#from sys import argv #import argument vectors from command line

#script, filename = argv #argv's are given the variables script and filename in that order

#txt = open(filename) # declare variable txt which runs the function open on the filename in the argv
#opens the filename for the use of python into the variable txt
#print(f"Here is your file {filename}:") #tells you what it is doing
#print(txt.read()) # displays a read of txt - the variable containing the filename which has been opened

print("Type the filename again:")
file_again = input("> ") # requests user input with a placeholder >

txt_again = open(file_again) # declare variable to open the nominated filename

print(txt_again.read(20)) # output the file named
