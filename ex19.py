def cheese_and_crackers(cheese_count, boxes_of_crackers): # defines a function which expects the listed arguments
    print(f"You have {cheese_count} cheeses!") # prints result of first argument
    print(f"You have {boxes_of_crackers} boxes of crackers!") # prints result of second argument
    print("Man, that's enough for a party!") # filler text
    print("Get a blanket.\n") # filler text with new-line


print("We can just give the function numbers directly:") # info line
cheese_and_crackers(20, 30) # call function with provided arguments


print("OR we can use variables from our script:") # info
amount_of_cheese = 10 # set variable
amount_of_crackers = 50 # set variable

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # call funtion with variables as above


print("We can even do maths inside too:") # info
cheese_and_crackers(10+20, 5+6) # call function with inline maths


print("And we can combine the two, variables and maths:") # info
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # call of function with hybrid declared variables and maths operations


def calculate_price_exc_vat(net_price):
    vat=1.2
    before_vat = float(net_price) / float(vat)
    print(f"For a bill of £{net_price} after VAT:")
    print(f"The price before tax was £{float(before_vat)} and".lstrip())
    print(f"the VAT added was £{float(net_price) - float(before_vat)}.".lstrip())

paid = input("How much did you pay in £? ")

calculate_price_exc_vat(paid)
