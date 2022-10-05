# Week 6 Assignment Part 3

# Goal create a python script to calculate the expected genotype frequencies
# in a population under Hardy Weinberg equilibrium based on known grequenceis at a
# a gene with TWO alleles 

# get frequency of p as the input 
p = float(input())

# get q as the difference with p
q = 1 - p

# calculate and print predicted HWE frequencies 
print("Frequency of AA:", round(p**2, 2))
print("Frequency of Aa:", round(2*p*q, 2))
print("Frequency of aa:", round(q**2, 2))


