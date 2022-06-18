people = 30 # declare variable people
cars = 40 # declare variable cars
trucks = 15 # declare variable trucks


if cars > people: # are there more cars than people
    print("We should take the cars.")
elif cars < people: # if not, are there fewer cars than people?
    print("We should not take the cars.")
else: #if not (i.e they must be equal)
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks!")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide..")

if people > trucks:
    print("Alright, lets just take the trucks.")
else:
    print("Fine, let's stay home then.")
