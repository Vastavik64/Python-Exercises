# Format variables using a string.format() method.

textstr = "I have {totalmoney} rupees so I can buy {quantity} cars worth {price} rupees"       # create a string and mention variable names
print(textstr.format(totalmoney = 1000, quantity = 3, price = 450))                   # use stringname.format() and specify variables