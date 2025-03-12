#Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
#create an empty list to store numbers
inputed_numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    inputed_numbers.append(num)

duplicates = []
recorded = []
#used for loops and if-else function to check for duplicates
for num in inputed_numbers:
    if num in recorded and num not in duplicates:
        duplicates.append(num)
    else:
        recorded.append(num)

print("Numbers that have duplicates:")
for num in duplicates:
    print(num)