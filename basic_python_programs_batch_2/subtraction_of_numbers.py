#Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
#This is the first number
num1 = int(input("Enter Number: "))
for i in range(9):
    num2 = int(input("Enter Number: ")) #This will served as the remaining numbers
    num1 -= num2
    print(num1)