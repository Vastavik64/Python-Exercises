# Write a program to display all prime numbers within a range

start = int(input("Enter start of the range: "))
end = int(input("Enter end of the range: "))
print("Prime numbers between",start,"and",end,"are: ")
for num in range(start,end+1):                              #take the range according to the input that user entered
    if num > 1:                                 #prime number always start from 1 
        for i in range (2,num):                 #define the range of numbers starting from 2
            if num%i == 0:                      # check for the facors if the number has factors it will not be a prime number therfore break the loop
                break
        else:
            print(num)                          # otherwise simply print the number