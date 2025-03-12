#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

numbers = []

#asking for input until an invalid input is entered
while True:
    try:
        
        num = int(input("Enter a number: "))
        #add the number to the list
        numbers.append(num)
        
    except ValueError:
        
        print("Invalid input! Exiting.")
        break
    #to sort the list from highest to lowest (descending order)
numbers.sort(reverse=True)

print("Numbers from highest to lowest:", numbers)