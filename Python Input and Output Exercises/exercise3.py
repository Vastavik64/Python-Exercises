# Convert Decimal number to octal using print() output formatting

number = int(input("Enter a decimal number: "))

if (number<=7):
    print("Octal number is: ", number)
else:
    Quotient = int(number/8)
    Reminder = int(number%8)
    i = 1
    while(i<8):
        Quotient[i] = int(Quotient/8)
        Reminder[i] = int(Quotient%8)
        i = i+1
    print("Octal number is: ", Reminder[i])