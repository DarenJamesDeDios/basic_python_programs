#Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
#initialized for the compilation of numbers
inputed_numbers = []
#ask for user input
for i in range(10):
    number = int(input("Enter Number: "))
    inputed_numbers.append(number)
#another list for checking duplicate purposes, keeping track of the numbers
numbers_displayed = []
#displaying the numbers 
print("Numbers displayed (only first entry counts):")
for number in inputed_numbers:
    if number not in numbers_displayed:
        print(number)
        numbers_displayed.append(number)
