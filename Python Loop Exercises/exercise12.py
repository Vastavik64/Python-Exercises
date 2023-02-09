# Display Fibonacci series up to 10 terms

num1 = 0                    # number 1 is always 0
num2 = 1                    # number 2 is always 1
for i in range(1,11):       # define the range
    print(num1,end=' ')     #print the first number and leave some space
    add = num1+num2         # add numbers
    num1 = num2
    num2 = add              # update value