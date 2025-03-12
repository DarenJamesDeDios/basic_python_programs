#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
#create a list to store numbers
inputed_numbers = []

while True:
    try:
        number = int(input("Enter a number: "))
        inputed_numbers.append(number)
        
    except ValueError:
        print("Invalid input, Try Again!") #To break the loop 
        break
