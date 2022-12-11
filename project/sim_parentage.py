
## Simulate parentage assignment depending on number of SNPs used

# import libraries
import random as rd
import numpy as np
import pandas as pd

# define parameters & initialize holder lists ----

# define possible values for SNPs
snp_values = ["A","T","C","G"]

# define size of parental population 
n_parents = 200

# define number of SNPs
n_snps = 100

# define list of SNP positions
snp_positions = list(range(n_snps))

# define number of replicates per percentage of SNPs removed 
reps = 10

# define percentages to remove
percentages_removed = np.arange(0.01,0.99,0.01).tolist()

# define lists to append values 
rm_snps = []
correct_parentage = []

## define functions used within the loop

# define a function to find the number of matches between 2 sequences
def find_matches(list_a, list_b):

    # define empty matches offspring
    matches = []

    # loop through first list 
    for i in range(len(list_a)):

        # if elements of the list match add 1 to matches if not add 0
        if list_a[i] == list_b[i]:
            matches.append(1)
        else:
            matches.append(0)
    return(sum(matches))

# define function to get mean 
def mean(lst):
    return sum(lst)/len(lst)

# simulation loop ---

for i in range(len(percentages_removed)):

    # define the percentage removed for this simulation run
    p_removed = percentages_removed[i]

    # start loop for each replicate
    for j in range(reps):

        # step 1: generate parental population

        # generate empty list to store parental population SNPs and info
        parent_snps = []
        parent_id = []

        # loop to generate parental population
        for x in range(n_parents):

            parent_snps.append(rd.choices(snp_values, k = n_snps)) # generate and add parent snps
            parent_id.append(x) # generate and add parent id

        # step 2: generate offpsring 

        # generate empty list to store offspring parent ID and offspring population
        offspring_parents = []
        offspring_snps = []

        # loop to generate offspring population
        for x in range(n_parents):
            
            # pick a random parent
            offspring_parent_id = rd.choice(parent_id)

            # attach parent 
            offspring_parents.append(offspring_parent_id)

            # generate and add offspring SNP as perfect copy of parents
            offspring_snps.append(parent_snps[offspring_parent_id])

        # step 3: reduce the number of snps

        # calculate the number of SNPs that are removed
        n_removed = round(n_snps * p_removed) # I need to round here to get a count

        # determine the SNPs that should be removed
        positions_removed = rd.sample(snp_positions, n_removed)

        # initialize lists for parent and offspring SNPs subsampled
        parent_snps_sub = []
        offspring_snps_sub = []

        # loop to filter snps
        for x in range(n_parents):

            # select the parent and offspring snps
            p_snps = parent_snps[x]
            o_snps = offspring_snps[x]

            # loop to assign "x" to snps that should be removed
            for y in range(len(positions_removed)):

                # assign the value of "x" to indicate removal
                p_snps[y] = "x"
                o_snps[y] = "x"

            # remove elements from both lists equaling X
            p_snps = [z for z in p_snps if z != "x"]
            o_snps = [z for z in o_snps if z != "x"]

            # append updated list
            parent_snps_sub.append(p_snps)
            offspring_snps_sub.append(o_snps)
        
        # step 4: assign parentage

        # generate an empty list to store assigned parentage
        offspring_assigned_parents = []

        # find matches between each offspring and all parents and find best parent match 
        for x in range(n_parents): # offspring number = parent number, could be changed in the future

            # object to store each offspring's matches
            matches = []

            # loop to find number of matches between one offspring and all parents
            for y in range(n_parents):

                # find matches between that offspring and each specific parent
                matches.append(find_matches(offspring_snps_sub[x], parent_snps_sub[y]))

            # find index for the best match
            offspring_assigned_parents.append(matches.index(max(matches)))

        # step 5: determine how well was parentage assigned

        # initialize empty list to store correctly assigned parentage
        correct_parentages = []

        # find percentage of parentage assigned correctly
        for i in range(len(offspring_assigned_parents)):

            if offspring_assigned_parents[i] == offspring_parents[i]:
                correct_parentages.append(1)
            else:
                correct_parentages.append(0)  

        # step 6: store values 

        # determine correct parentages
        correct = mean(correct_parentages)

        # append results
        rm_snps.append(p_removed)
        correct_parentage.append(correct)

# tidy output ----

# turn into a dictionary 
d = {'percentage_snps_rm': rm_snps, 'correct_parentage': correct_parentage}

# turn into a pandas dataframe
df = pd.DataFrame(data = d)

print(df)

# save as a csv
from pathlib import Path  
filepath = Path('out_test.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True) 
df.to_csv(filepath)  


