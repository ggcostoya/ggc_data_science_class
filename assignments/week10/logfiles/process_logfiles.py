## Week 10 Assignment

import re
import sys
import codecs
import pandas as pd

# open output file 
#out = open("log_output.txt", 'w') # 

# generate empty pandas dataframe to store output 
log_data  = pd.DataFrame(list(zip([],[],[],[],[])), columns = ["log_id","day", "time", "ampm","temp"])

# genereate control variable to count number of files processes
files_processed = 0

# start of the loop reading every .txt file in the folder
for file in sys.argv[1:]:

    # get input
    input = codecs.open(file, 'r', encoding='utf-8', errors='ignore')

    # extract the logger id for that file
    log_id = re.sub('.txt.txt',"", file)

    # define empty objects to store data 
    log_id = []
    days = []
    time = []
    ampm = []
    temp = []

    # start loop reading line by line 
    for line in input:
        line = line.strip("\n") # remove line endings
        line = line.replace("\0", "") # clean problematic characters
        split = line.split() # split all elements in a line
        log_id.append(log_id) # append logger id
        days.append(split[1]) # append day info
        time.append(split[2]) # append time info
        ampm.append(split[3]) # append ampm info
        temp.append(split[4]) # append temp

    # create a list a list of lists where each list contains the info below
    lists = list(zip(log_id, days, time, ampm, temp))

    # transform list of lists into pandas data frame
    df = pd.DataFrame(lists, columns = ["log_id","day", "time", "ampm","temp"])

    # remove the first row of data frame (contains row names)
    df = df.iloc[1: , :]

    # concatenate pandas data frame to holder data frame
    log_data = pd.concat([log_data,df])

    # check messages
    files_processed += 1
    print(files_processed)

    # close input
    input.close()

# save output
log_data.to_csv('log_output.txt')

# write output
#out.write(log_data)

# close output
#out.close()

