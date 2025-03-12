#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
#initialize list for storing numbers
inputed_numbers = []
while True:
    try:
       numbers = int(input("Please enter a number: "))
       inputed_numbers.append(numbers)  #add the number to the list if it's valid
    except ValueError:
        #makes it exit if the number is invalid
        print("Invalid input! Enter an appropriate number please.")
        break
if numbers:  
    average = sum(numbers) / len(numbers)  #calculate the average
    print(f"The average of the entered numbers is: {average}")

