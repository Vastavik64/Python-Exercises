# Count the total number of digits in a number

number = int(input("Enter a number: "))                 #ask user for the number
counter = 0                                        # take a variable to keep a count of digits and set it initially to zero
while(number!=0):                                 # take a while loop until the number is not equal to zero
    number = number//10                         # perform floor division of the number by ten which will count each digit in it
    counter = counter+1                          # increase the counter
print(counter)