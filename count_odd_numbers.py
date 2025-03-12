#Create a program that ask user to input 10 numbers. Print how many are odd numbers.
#Initialized
oddnum = 0
#Ask for user input
for i in range(10):
    num = int(input("Enter Number: "))
    
#Count odd numbers
    if num % 2 != 0:
     oddnum += 1
print(oddnum)
