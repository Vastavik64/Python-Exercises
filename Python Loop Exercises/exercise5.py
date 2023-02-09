# Display numbers from a list using loop

lst = [12, 75, 150, 180, 145, 525, 50]                     # create a list
print("Numbers that satisfy conditions are: ")
for item in lst:                                    # take each number or item from the list
    if item > 500:
        break                                       # break is used to terminate the loop
    if item > 150:
        continue                                   # coninue is used to skip an iteration
    if item % 5 == 0:                              # check divisibility by five
        print(item)