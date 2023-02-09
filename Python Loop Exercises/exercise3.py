# Calculate the sum of all numbers from 1 to a given number

num = int(input("Enter a number: "))               #take input from user
print("Summation is: ")
sum = 0                                           # take a variable with defaultt value zero to store the summation
for i in range(1,num+1,1):                        # define range of number with i as the current digit for each iteration
    sum = sum+i                                   # summation would be sum+current number i.e i
print(sum)