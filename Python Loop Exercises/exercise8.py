# Print list in reverse order using a loop

lst = [10, 20, 30, 40, 50]                      #create a list
length = len(lst) - 1                           #obtain length of the list and subtract one from it
for i in range(length,-1,-1):                   #reverse the index numbers of the list
    print(lst[i])