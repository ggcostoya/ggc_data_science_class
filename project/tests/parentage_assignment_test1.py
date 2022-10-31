# Generate Parental Population 

# import packages? libraries?
import random

# define list of bases
bases = ["A","T","C","G"]

# define number of individuals on parental population 
n_parents = int(input("Number of Parents: "))

# define number of snps per individual
n_snps = int(input("Number of SNPS: "))

# generate empty object to store parental population snps 
# and ids
parents_snps = []
parents_id = []

# loop to generate parental population
for i in range(n_parents):

    # generate and add parent snps
    parents_snps.append(random.choices(bases, k = n_snps))

    # add parent id 
    parents_id.append(i)

# generate an empty list to store offspring snps, ids and true parentage
offspring_snps = []
offspring_id = []
offspring_parents = [] # actual parents

# generate offspring population (equal size as parental)
for i in range(n_parents):

    # pick random parent
    offspring_parent_id = random.choice(parents_id)

    # attach assigned parents to the actual parents list
    offspring_parents.append(offspring_parent_id)

    # generate and add offspring snps as a perfect copy of parents
    offspring_snps.append(parents_snps[offspring_parent_id])

    # add ofspring id
    offspring_id.append(i)

# generate vector to store assigned parentage
offspring_assigned_parents = []

# define function to find number of matches
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

# find matches between each offspring and all parents 
for i in range(n_parents): # offspring number = parent number, could be changed in the future

    # object to store each offspring's matches
    matches = []

    # loop to find number of matches between one offspring and all parents
    for j in range(n_parents):

        # find matches between that offspring and each specific parent
        matches.append(find_matches(offspring_snps[i], parents_snps[j]))

    # find index for the best match
    offspring_assigned_parents.append(matches.index(max(matches)))

# empty object for correctly assigned parentage
correct_parentages = []

# define function to get mean 
def mean(lst):
    return sum(lst)/len(lst)

# find percentage of parentage assigned correctly
for i in range(len(offspring_assigned_parents)):

    if offspring_assigned_parents[i] == offspring_parents[i]:
        correct_parentages.append(1)
    else:
        correct_parentages.append(0)        

# final output
print("Percentage of parentages assigned correctly is:", mean(correct_parentages)*100, "%")