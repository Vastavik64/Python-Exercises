# Read line number 4 from the following file

with open('text.txt', 'r') as tr:                 # open file in reading mode
    lines = tr.readlines()                        # read each line from the file
    print(lines[3])                               # display line number four from the file