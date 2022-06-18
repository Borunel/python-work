formatter = "{} {} {} {}" #creates a variable string with four empty locations

print(formatter.format(1, 2, 3, 4)) # prints the formatter and formats the locations with four numbers
print(formatter.format("one", "two", "three", "four")) # prints the formatter and formats the locations with four strings
print(formatter.format(True, False, False, True)) # prints the formatter and formats the locations with four booleans
print(formatter.format(formatter, formatter, formatter, formatter)) # prints the formatter and formats the locations with four of the original variable which returns the curly brackets as strings
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "or a song about fear"
)) #again prints the variable string with the empty locations filled with longer strings - which all display on a single line
