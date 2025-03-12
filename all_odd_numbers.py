#Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
oddnum = 0
while oddnum < 100:
    if oddnum % 2 != 0:
        print(oddnum)
        oddnum += 1
