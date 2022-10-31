
# Week 9 Assignment

# import libraries
import re
import sys

# Task 1 ---

# based on the examples I am going to assume we are dealing with the Manacus genome
# but this coould be applied to any fasta sequence. 
in1 = open(sys.argv[1], "r")

# defining global variables
seq_no = 0 # number of sequences
EcoRI = 0 # number of GAATTC cut sites
Mse1 = 0 # number of TTAA cut sites
HindIII = 0 # number of AAGCTT cut sites

# loop to extract information
for line in in1:
    seq = in1.readline() # read file line by line
    seq = seq.strip("\n") # separate by line endings 
    seq_no +=1 # add one to the number of sequences counter
    EcoRI += len(re.findall("GAATTC", seq)) # EcoRI cut site counter
    Mse1 += len(re.findall("TTAA", seq)) # Mse1 cut site counter
    HindIII += len(re.findall("AAGCTT", seq)) # HindII cut site counter

print("Task 1:")
print("File has %d sequences, %d EcoRI, %d Mse1 and %d HindIII cut sites \n" % (seq_no, EcoRI, Mse1, HindIII))

# Task 2 ----

# define input and output 
in2 = open(sys.argv[1], "r")
out1 = open(sys.argv[2], "w")

# loop to extract information
for line in in2:
    line = line.strip("\n") # get sequence id
    fasta = line # store sequence id
    seq = in2.readline() # read sequences line by line
    seq = seq.strip("\n") # separate line endings
    # if statement to check only sequences that have the repeats
    if re.search(r"(AT){4,}", seq) or re.search(r"(ATC){4,}", seq) or re.search(r"(GA){4,}", seq):
        ATs = len(re.findall(r"(AT){4,}", seq)) # count AT repeats
        ATCs = len(re.findall(r"(ATC){4,}", seq)) # count ATC repeats
        GAs = len(re.findall(r"(GA){4,}", seq)) # count GA repeats
        out1.write("%s contains %d ATs, %d ATC and %d GA x4 repeats \n" % (fasta,ATs,ATCs,GAs)) # write output
