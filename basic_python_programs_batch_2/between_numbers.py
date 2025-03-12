#Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
while num1 < num2:
    print(num1)
    num1 += 1
    if num1 == num2:
        break