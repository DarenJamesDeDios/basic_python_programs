#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
inputed_numbers = []
#used while function to start a loop infinitely asking input
while True:
    try:
       user_input = int(input("Please enter a number: "))
       numbers.append(num)  # Add the number to the list if it's valid
    except ValueError:
        # If conversion fails (invalid input), exit the loop
        print("Invalid input!")
        break

