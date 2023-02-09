# Print the following pattern

rows = 5
cols = 5
# Forward pattern
for i in range(1,rows+1,1):
    for j in range(1,i+1):
        print("*", end='')
    print(' ')
# Reverse pattern
for i in range(1,rows+1):
    for j in range(cols-i,0,-1):
        print("*", end='')
    print(' ')