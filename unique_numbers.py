#Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
numbers = []
while True:
    try:
        number = int(input("Enter Number: "))
        if number in numbers:
            print("Duplicate")
        else:
            print("Unique")
    except ValueError:
        break

