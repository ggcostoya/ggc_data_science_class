
# Week 8 Assignment

# Import libraries 
import readline
import sys
import re
#import numpy
#import pandas

# Part 1. ----

# opening input file
in_file = open('genenames.txt', 'r')

# reading and splitting the file 
in_file_list = in_file.read().split()

# read columns one and 2
col1 = in_file_list[::1]
col2 = in_file_list[::2]

# print contents of column 2
print("Part 1:",col2)

## Part 2. ----

# open input file
flies = open('flies.txt', 'r')

# open output file
#flies_out = open('flight_times.txt', 'w')

# empty list to store flight times
flight_times_d = []

# loop to extract flight times
for line in flies:
    line = line.strip('\n') # remove line endings
    elementlist = line.split('\t') # split each list
    if elementlist[1] == "D": # if during the day
        flight_times_d.append(elementlist[2]) # append flight time
    else: # if during night pass
        pass

# print flight times during day to check
print("Part 2 check:", flight_times_d)

# write output
#flies_out.write(str(flight_times_d) + "\n")

## Part 3 ----

# input file 
#seq_input = open('no60_intron_IME_data.fasta', 'r')
seq_input = open(sys.argv[1], 'r')

# Note: For some reason I just can't use sys.argv to import files.

# read contents into a single scalar
#seq = seq_input.read().split('>')

seq = seq_input.read().split('>')

# remove all empty elements of the list
seq = list(filter(("").__ne__, seq))

print(len(seq))

# empty vector to store list of results
results = []

# loop to extract information from each sequence
for x in range(len(seq)):
    lx = seq[x] # extract the first line
    lx = lx.split('\n') # separate information
    seq_id = lx[0] # get the sequence id
    seq_len = len(lx[1]) # get the length of the sequence
    seq_gnc = len(re.findall("G",lx[1])) + len(re.findall("C",lx[1])) # find all Gs and Cs
    seq_info = list[seq_id, seq_len, seq_gnc]
    results = list[results,seq_info]


print(results[0:1])


#l1 = seq[0]

#l1 = l1.split('\n')

#sequence_id = l1[0]

#length_sequence = len(l1[1])

#gcs = len(re.findall("G",l1[1])) + len(re.findall("C",l1[1]))

#result = list[sequence_id, length_sequence, gcs]

#print(results[0])

