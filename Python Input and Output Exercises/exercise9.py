# Check whether file is empty or not
import os
with open('test.txt', 'r') as tr:
    tr.readlines()
    tr.close()
siz = os.stat('test.txt').st_size
if siz == 0:
    print("The file is empty")
else:
    print("The file is not empty")