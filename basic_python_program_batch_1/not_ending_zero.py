#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
for numbers in range(101):
    if numbers % 10 != 0:
        print(numbers)
#I think i'll use for-loop here too