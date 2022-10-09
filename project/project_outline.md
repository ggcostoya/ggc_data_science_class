# Project Plan

## Background

A fundamental piece of information to have when conducting evolutionary studies are the parentage relationships between individuals of the population being studied. For instance, parentage information provides a way to asses the effects of natural selection by comparing reproductive success between individuals as a function of phenotypic differences. In the abscence of constant surveilling, parentage assignment is achieved by comparing a sample of unlinked, independent genomic markers (e.g., SNPs) between multiple individuals. Considering more of these genomic markers reduces the uncertainty of parentage assigning. However, sequencing is costly, so there is a balance to be found between the number of microsatellites or SNPs sequenced and the certainty associated with parentage assignment.

## Goal

Determine the relationship between the number of SNPs considered and the uncertainty in parentage assigning (i.e., the probability of correctly assigning the parents of a given individual).

## Methodology

Below are the steps I will temptatively follow. Needless to say that all necessary code will be written in **Python** and run through a **Linux terminal** as we have been doing in class. 

1. **Generate a parental population**: Generate a sample of $N$ individuals where each individual is represented by a set of $N_{SNP}$. I will set $N_{SNP}$ as a large enough number such that it is representative of an individual's entire genotype. For simplicity, I will assume that individuals are **haploids** such that each SNP is represented by a single nucleotide among *A*,*T*,*C*,*G*. 

    > **NOTE**: I am open to the possibility of making individuals diploids and of different sexes, but if I do, I am worried that the project might take too much of my time. If I find out it is relatively easy I'll change to make things more realistic. 

2. **Generate an offspring population**: Generate a sample of $M$ individuals  that are the offspring of the parental population. For each new individual within $M$, I will sample $2$ random individuals within $N$ as parents. The new individual will inherit either of the parents alleles with equal probability to generate its sequence of unique $N_{SNP}$. Afterwards, I will store the identity of the parents for posterior checks. 

3. **Re-obtain genetic information**: To compare the effects of considering more or less SNPs when assinging parentage, for each individual in $N$ and $M$ I will run multiple trials sampling a percentage $P$ among all $N_{SNP}$. $P$ will assume different values between 0 to 1 ranging from 10 to 100% of $N_{SNP}$. 

4. **Assess parentage**: For each trial considering a particular $P$, I will use the methodology developed by **Grashei et al. 2018** (https://gsejournal.biomedcentral.com/articles/10.1186/s12711-018-0397-7) to asses parentage between all individuals. Once parentages are assigned, I will compare them to the list of true relationships stored initially to assess the percentage of relationships assigned correctly. 

5. **Replicates**: I will run steps 1 through 5 as part of a simulation run which I will repeat $R$ times in order to offer more solid conclusions. For start, I will set $R = 10$ and if it turns out that the code is fast enough I'll go to $R = 100$ or more. 

## Expected Outcomes

A good sense of what is the minimum genetic markers needed to establish credible parentage assignations. I expect the percentage of parentage relationships assigned correctly to plateau at a high rate when $P < 0.9$ so I am curious to see how low will that number be. Furthermore, this code might serve as the foundation for assigning parentage on my own experimental populations or to better understand how existing pipelines to do the same work. 





