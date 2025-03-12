#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
inputed_numbers = []
#used while function to start a loop infinitely asking input
while True:
    try:
       numbers = int(input("Please enter a number: "))
       inputed_numbers.append(numbers)  # Add the number to the list if it's valid
    except ValueError:
        # If conversion fails (invalid input), exit the loop
        print("Invalid input!")
        break
    #display the lowest one
if inputed_numbers:
    lowest = inputed_numbers[0]
    for numbers in inputed_numbers:
        if numbers < lowest:
            lowest = numbers
    print("The lowest number entered is:", lowest)

