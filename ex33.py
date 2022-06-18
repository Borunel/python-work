def nombre(i):

    numbers = []

    for i in range(0,i,1):
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


x = int(input("What is the limit? "))

nombre(x)
