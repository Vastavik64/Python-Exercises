# Find the factorial of a given number

num = int(input("Enter a number: "))            #take input from the user
print("Factorial of",num,"is: ")
pro = 1                                 # take a variable and assign value one to it as it is multiplication
for i in range(1,num+1):                # define the range
    pro = pro*i                         # multiply each number to the previous one
    i = i+1                             # increament by one
print(pro)                              # print the product