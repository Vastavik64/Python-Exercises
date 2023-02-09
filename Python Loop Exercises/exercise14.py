# Reverse a given integer number

num = int(input("Enter a number: "))
print("Entered number is: ", num)
rev_num = 0                             # take a variable which would be used to store the reversed number
while num>0:
    digit = num%10                      # define a variable to store the reminder of original number after division by 10
    rev_num = rev_num*10 + digit        # multiply the variable by 10 and add the obtained reminder
    num = num//10                       # perform float divison by 10
print("Reversed number is: ", rev_num)