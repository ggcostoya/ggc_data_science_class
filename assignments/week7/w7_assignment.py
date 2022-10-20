# Week 7 assignment

# Part 1

# copy line of code
DNA_Info = 'SAMPLE_110 Pop3 atatctcgcggggtttatatatattatttaaa'

# A. Get rid of everything other than the DNA sequence and save to another string

# A1. separate contents to assign string
DNA_Info = DNA_Info.split(" ")
print("Step 1 - A1:", DNA_Info)

# A2. select only DNA string and save into new string
DNA = DNA_Info[2]
print("Step 1 - A2:", DNA)

# B. Change the DNA sequence string to contain uppercase rather than lowercase
DNA = DNA.upper()
print("Step 1 - B:", DNA)

# C. Count the number of Gs, Cs, Ts

# C1. generate empty floats to fill up
As = 0
cs = 0
gs = 0
ts = 0

# C2. loop to fill the counts of each kind of base
for base in DNA:
    if (base == "A"):
        As += 1
    elif(base == "C"):
        cs += 1
    elif(base == "G"):
        gs += 1
    else:
        ts += 1

print("Step 1 - C:")
print("There are %d A bases" % (As))
print("There are %d T bases" % (ts))
print("There are %d C bases" % (cs))
print("There are %d G bases" % (gs))

# D. Reverse the order of the DNA sequence
Rev_DNA = DNA[::-1]
print("Step 1 - D:", Rev_DNA)

# Part 2

# copy line of code
DNA_Seq = 'A,C,G,T,A,A,A,T,G,C,C,A,T,G,C,C,G,G,A,A,T,C,G,A,T,T,T'

# A. Split string to generate a list 
DNA = DNA_Seq.split(",")
print("Step 2 - A:", DNA)

# B. Turn list back into a string
DNA_string = ''.join(DNA)
print("Step 2 - B:", DNA_string)

# C. Concatenate DNA sequences 

# new sequence 
SeqList2 = ['A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T']

# generate longer list 
Long_DNA_list = DNA + SeqList2
print("Step 2 - C:", Long_DNA_list)

# D. Make new list with only the 10 first bases of C sequence
SeqList2_10 = SeqList2[0:10]
print("Step 2 - D:", SeqList2_10)

# E. Print list length with if else conditionals
print("Step 2 - E:")

if(len(SeqList2_10) > 8):
    print("Length is greater than 8")
else:
    print("Length is NOT greater than 8")

# F. Print the final list in reverse order
print("Step 2 - F:", SeqList2_10[::-1])
print("Step 2 - F:", SeqList2_10.reverse)

# Part 3

# A. Make a simple list of integeres from 1 to 100
NumList=list(range(1,100))

# B. Using a for loop print each value, comma, value muliplied by 2, a comma,
# the element that value occupies in the list, a comma, and whether the original
# number is even or odd. 

print("Step 3 - B:")
for x in NumList:
    value = x
    value_2 = x*2
    index = NumList.index(x)
    if x%2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print("%d,%d,%d,%s" % (value,value_2,index,even_odd))

# C. Write output to a file

# in the command prompt I would type python3 w7_assignment > output.txt 
