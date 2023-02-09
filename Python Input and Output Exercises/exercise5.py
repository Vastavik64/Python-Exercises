# Accept a list of 5 float numbers as an input from the user

lst = []                     # create an empty list

num = int(input("Enter number of elements in the list: "))         # take number of elements in the list

for i in range (0, num):
    elemen = float(input("Enter a float element: "))         # take element value from the user      

    lst.append(elemen)            # append the element which means add the element at the last place in the list

print("The list is: ", lst)       # display the final list