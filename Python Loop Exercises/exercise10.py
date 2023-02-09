# Use else block to display a message “Done” after successful execution of for loop

n = int(input("Enter range of the loop: "))

for i in range(n+1):                #define range of for loop as i
    print(i)                        #print the numbers of loop
if i == n:                          # if last number equals the entered input then print done
    print("Done!")
else:                               # if last number not equals the entered input then print not done
    print("Not done")