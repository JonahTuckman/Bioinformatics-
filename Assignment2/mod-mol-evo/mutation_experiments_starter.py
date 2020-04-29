#-----------------------------------------------------------------
# BIOL/CMPU-353
# Spring 2020
# Modeling Molecular Evolution
# Mutation Experiments
# Written by: Marc Smith and Jodi Schwarz
# Modified by: Jonah Tuckman
#
# Description:
#   This program runs computational experiments to measure how
#   mutating a DNA sequence in different ways results in different
#   similarity measures between original and mutated sequences.
#   
#   Both mutation strategies require mutating 15% of the original
#   DNA sequence, with the following differences:
#   - one strategy mutates nucleotides occurring anywhere in the 
#     sequence
#   - the other strategy targets only nucleotides in the third 
#     position of a codon
# 
#   Which strategy will more greatly impact the similarity between 
#   original and mutated protein sequences?
#-----------------------------------------------------------------


import re
import random
from Bio import pairwise2
from Bio.pairwise2 import format_alignment 

# Global variables

path = "/home/jttuckman/Bioinformatics-/Assignment2/mod-mol-evo/"  # replace mlsmith with your id
aa_codon_filename = path + "aa-codon-table.txt"

codon_map = {}                           # dictionary: codon->AA
TRIALS = 100                             # no. of experimental trials
MUTATION_RATE = .15                      # mutation rate

nuc_file = path + "hsp70_nuc.fasta.txt"  # files containing
aa_file = path + "hsp70_aa.fasta.txt"    # DNA and protein sequences

orig_DNA_seq = ""                        # strings to hold original
orig_prot_seq = ""                       # DNA and protein sequences

#############################################################################
# main function: called at bottom of file
#############################################################################
def main():
	
    # Initialize DNA and protein sequences from data files
    orig_DNA_seq = read_fasta_file( nuc_file )
    orig_prot_seq = read_fasta_file( aa_file )

    create_codon_map()

    # Conduct TRIALS no. of experiments using strategy 1
    print("Results for random mutation strategy\n")
    print("Trial, % identity\n")
    for trial in range(TRIALS):
        percent_id = strategy1( orig_DNA_seq, orig_prot_seq)
        print(str(trial+1) + ", " + str(percent_id))
    print("\n")

    # Conduct TRIALS no. of experiments using strategy 2
    print("Results for random mutation strategy\n")
    print("Trial, % identity\n")
    for trial in range(TRIALS):
        percent_id = strategy2( orig_DNA_seq, orig_prot_seq)
        print(str(trial+1) + ", " + str(percent_id))
    print("\n")


#############################################################################
# strategy1
# Perform a single experiment using strategy 1: 
#   mutates 15% of nucleotides 
#############################################################################
def strategy1(orig_DNA_seq, orig_prot_seq):
    # build new sequence
    new_DNA_seq = "";
    for nuc in orig_DNA_seq:
        if (random.random() < MUTATION_RATE):
            # randomly mutate nuc to a new nucleotide (A, C, G, T)
            new_DNA_seq = new_DNA_seq + rand_nuc(nuc)
        else:
            # append original nucleotide to new sequence
            new_DNA_seq = new_DNA_seq + nuc

    # translate new DNA sequence to protein sequence
    new_prot_seq = translate( new_DNA_seq )

    # calculate the percent identity 
    identity = calc_identity( new_prot_seq, orig_prot_seq )

    return identity

#############################################################################
# strategy2 
# Perform a single experiment using strategy 2:
#   Mutates 15% of nucleotides in third positions of codons 
#############################################################################
def strategy2(orig_DNA_seq, orig_prot_seq):  
    new_seq = ""
    count = 0
    for nuc in orig_DNA_seq:
        #count += 1
        if count % 3 == 2: 
            if (random.random() < ( MUTATION_RATE * 3)):
                new_seq = new_seq + rand_nuc(nuc)
            else:
                new_seq = new_seq + nuc

        else:
            new_seq = new_seq + nuc
        
        count += 1

    new_prot = translate(new_seq)

    identity = calc_identity(new_prot, orig_prot_seq)
       # count += 1

    return identity


#############################################################################
# calc_identity
# calculates the percent identity of the two given sequences.
#############################################################################
def calc_identity(seq1, seq2):
    count = 0
    #for i in range(0, len(seq1)):
     #       arr = seq2[:,i]
      #      if arr == len(arr) * arr[0]:
       #         count += 1

    length = len(seq1)
    # zip the two sequences 
    for n1, n2 in zip(seq1, seq2):
        if n1 == n2:
            count += 1


    # align = pairwise2.align.globalms(seq1, seq2, 2, -1, -0.5, -0.1)

    #maxx = 0
    #for i in align: 
     #   if format_alignment(*i) > maxx:
      #      maxx = format_alignment(*i)

    #return  maxx / 100

    return count / float(length)


#############################################################################
# rand_nuc 
# returns a random nucleotide from A, C, G, or T.
#############################################################################
def rand_nuc(original):
    condition = True
    while condition:
        choice = random.choice( ['A', 'C', 'T', 'G'] )
        if choice != original:
            condition = False
    return choice



#############################################################################
# create_codon_map 
# initializes dictionary for aa lookups by codon
#############################################################################
def create_codon_map():
    in_file = open(aa_codon_filename, 'r')

    for line in in_file:
        aa_list = line.split()
        aa = aa_list[0]
        for codon in aa_list[1:]:
            codon_map[codon] = aa 

    in_file.close()


#############################################################################
# translate 
# translates DNA strings to proteins
#############################################################################
def translate( DNA ):
    pro = ""
    for codon in re.findall('(...)', DNA):
        pro = pro + codon_map[codon]
    return pro


#############################################################################
# read_fasta_file 
# read fasta file containing single sequence, return sequence
#############################################################################
def read_fasta_file( filename ):
    in_file = open(filename, 'r')
    in_file.readline()	# ignore tag line
	
    sequence = ""		# read and concatenate sequence lines
    for line in in_file:
        sequence = sequence + line.rstrip('\n')

    in_file.close()
    return sequence

main()
