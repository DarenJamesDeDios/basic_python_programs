#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
#asking continuously until invalid
while True:
    try:
        # Ask user for input
        num = int(input("Enter a number: "))
    except ValueError:
        break