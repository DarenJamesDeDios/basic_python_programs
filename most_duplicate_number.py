#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicat
numbers = []

#continuously asking for user input
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)                  #adds them on the list
        
    except ValueError:
        print("Invalid input! Exiting.")
        break
if numbers:
    #in order to track the most common number and its count
    most_common_num = None
    most_common_count = 0
    for num in numbers:
        count = numbers.count(num)
        #if there is more than the other this serve as the update 
        if count > most_common_count:
            most_common_count = count
            most_common_num = num
            