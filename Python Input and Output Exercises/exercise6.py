# Write all content of a given file into a new file by skipping line number 5
# Note: files for operation must be in the same folder as program otherwise specify location

with open('text.txt', 'r') as tr:                 # open file in reading mode
    lines = tr.readlines()                        # read each line from the file
with open('new_file.txt', 'w') as tr:             # open file in write mode
    counter = 0                                   # take a variable to keep the count of each line and set it initially to zero
    for line in lines:                            # run a for loop considering each line from all the lines in old file
        if counter == 4:                          # select the line which needs to be skipped
            counter = counter + 1                 # increament the counter by one to proceed to the next line
            continue                              # use continue to skip a line
        tr.write(line)                            # write each line into the new file
        counter += 1