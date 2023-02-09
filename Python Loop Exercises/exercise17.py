# Find the sum of the series upto n terms

n = int(input("Enter number of terms: "))           # take input from user
start = 2                                   # set a variable as 2
seq = 0                                     # declare a variable to store the final answer
for i in range(0,n):
    print(start,end='+')                    # print start and symbol +
    seq = seq+start                         # add previous numbers and store the result in seq
    start = start*10+2                      # update the value of start with each iteration using this formula
print("  Summation is: ", seq)              # print the final answer