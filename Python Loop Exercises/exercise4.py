# Write a program to print multiplication table of a given number

num = int(input("Enter a number: "))
print("Multiplication table of",num, "is: ")
pro = 1
for i in range(1,11):
    pro = num*i
    print(pro)