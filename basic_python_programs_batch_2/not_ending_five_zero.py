#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
for numbers in range(101):
    if numbers % 5 != 0:
        print(numbers)