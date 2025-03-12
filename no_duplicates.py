#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

#create an Empty list for storing numbers
inputed_numbers = []
#ask for user input
for i in range(10):
    number = int(input("Enter Number: "))
    inputed_numbers.append(number)
#checking for duplicates
recorded = []
duplicates = []
for number in inputed_numbers:
    if number not in recorded:
        recorded.append(number)  #add the number to 'recorded' if it hasn't been recorded before
    else:
        if number not in duplicates:
            duplicates.append(number)  #add to 'duplicates' if it has appeared before
#displaying the numbers that don't have duplicates
print("Numbers that don't have duplicates:") 
for number in recorded:
    if number not in duplicates:
        print(number)


