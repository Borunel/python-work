print("Mary had a little lamb.") # print string
print("Its fleece was white as {}.".format('snow')) # print string but insert extra string (its just a string because it only has inverted commas not quotation marks) at empty curly braces
print("And everywhere that Mary went.") # print string
print("." * 10) # what did that do? printed the string ten times

end1 = "C" # allocate string to variable
end2 = "h" # allocate string to variable
end3 = "e" # allocate string to variable
end4 = "e" # allocate string to variable
end5 = "s" # allocate string to variable
end6 = "e" # allocate string to variable
end7 = "B" # allocate string to variable
end8 = "u" # allocate string to variable
end9 = "r" # allocate string to variable
end10 = "g" # allocate string to variable
end12 = "r" # allocate string to variable
end11 = "e" # allocate string to variable

# watch that comma at the end. Try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ') # print first six variable plus some type of instruction to stay on the same line with a space?
print(end7 + end8 + end9 + end10 + end11 + end12) # Print the remaining variables (strings)
# if you remove the "end = ' ' " then line line 21 prints on the next line
