from sys import argv # summons module argv from sys

script, input_file = argv # argv is script and input file in that order

def print_all(f): # define function print_all with single argument
    print(f.read()) # print content of f which is a filename

def rewind(f): # define function rewind
    f.seek(0) # sets position of file handle (cursor) to a certain offset from a reference position f.seek(offset,from_what)
# 0=start of file, 1=current position, 2= end of file - by default zero. offest is number of positions so here we have zero posn from the start

def print_a_line(line_count,f): # define function print_a_line
    print(line_count, f.readline()) # prints number of current line and a read of that line

current_file = open(input_file) # opens input file from argv and sets content to current_file

print("First lets print the whole file.\n") # info line

print_all(current_file) # prints content from 14

print("Now lets rewind, kind of like a tape.") # info

rewind(current_file) # calls rewind function on current_file

print("Lets print three lines.") # info

current_line = 1 # declares variable current_line as 1
print_a_line(current_line, current_file) #calls function current_line  with declared line number and readline of current _file

current_line += 1 # increment current_line by 1
print_a_line(current_line, current_file) #print next line

current_line += 1 # increment current_line by 1
print_a_line(current_line, current_file) #print next line
