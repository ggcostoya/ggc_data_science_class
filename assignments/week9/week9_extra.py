
# Week 9 Extra Assignment

# import libraries
import re
import sys

# get argument list length
n_args = len(sys.argv)

for x in range(1, n_args):

    input_name = sys.argv[x] # store input name
    input = open(sys.argv[x], "r") # opn input

    # define global variables
    cut_sites = 0
    repeats = 0

    # loop to count cut sites and repats
    for line in input:
        seq = input.readline() # read input line by line
        seq = seq.strip("\n") # separate line endings
        EcoRI = len(re.findall("GAATTC", seq)) # EcoRI cut site counter
        Mse1 = len(re.findall("TTAA", seq)) # Mse1 cut site counter
        HindIII = len(re.findall("AAGCTT", seq)) # HindII cut site counter
        cut_sites += EcoRI + Mse1 + HindIII # total cut site number 
        ATs = len(re.findall(r"(AT){4,}", seq)) # count AT repeats
        ATCs = len(re.findall(r"(ATC){4,}", seq)) # count ATC repeats
        GAs = len(re.findall(r"(GA){4,}", seq)) # count GA repeats
        repeats += ATs + ATCs + GAs # total repeats number

    # print output
    print("%s has %d cut sites and %d repeats \n" % (input_name, cut_sites, repeats))

