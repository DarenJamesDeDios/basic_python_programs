#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
inputed_numbers = []
while True:
    try:
       numbers = int(input("Please enter a number: "))
       inputed_numbers.append(numbers)  #add the number to the list if it's valid
    except ValueError:
        #makes it exit if the number is invalid
        print("Invalid input!")
        break
    #checking the highest one
if inputed_numbers:
    highest = inputed_numbers[0]
    for numbers in inputed_numbers:
        if numbers > highest:
            highest = numbers