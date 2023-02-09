# Use a loop to display elements from a given list present at odd index positions

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]             # create a list
n = len(lst)                                                # obtain the length of the list
for i in range(1,n+1):                                      # define the range
    if i%2 == 0:                                            # if index number is even then skip it
        continue
    else:
        print(lst[i])                                       # print the remaining elements of the list