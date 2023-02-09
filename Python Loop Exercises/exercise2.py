# Print the following pattern
rows = 5                                 #take number of rows
for i in range(1,rows+1,1):              # take range of i with one in the first as well as last position and rows would be increades by one
    for j in range(1,i+1):               # specify the range of j from zero to increament in i for each iteration
        # display the pattern
        print(j, end='')
    print(' ')