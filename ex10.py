tabby_cat = "\tI'm tabbed in. \n{}" # variable using a tab escape seq
persian_cat = "I'm split\non a line" # variable string using new line escape seq
backslash_cat = "I'm \\ a \\ cat" # variable using a backslash escape seq

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass\b
''' # string demonstrating use of triple quotes, tab escape seq and new line

# bell_end = "This is a ASCII bell apparently: \a" #makes an error sound
dont_like = "I don't like it"

print(tabby_cat.format(dont_like))
print(persian_cat)
print(backslash_cat)
print(fat_cat)
#print(bell_end)
