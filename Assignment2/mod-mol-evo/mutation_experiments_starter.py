#-----------------------------------------------------------------
# BIOL/CMPU-353
# Spring 2020
# Modeling Molecular Evolution
# Mutation Experiments
# Written by: Marc Smith and Jodi Schwarz
# Modified by: <your name here>
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

# Global variables

path = "/home/mlsmith/bioinf/mod-mol-evo/"  # replace mlsmith with your id
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
            new_DNA_seq = new_DNA_seq + rand_nuc()
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
	return 0.0


#############################################################################
# calc_identity
# calculates the percent identity of the two given sequences.
#############################################################################
def calc_identity(seq1, seq2):
    return 0.0


#############################################################################
# rand_nuc 
# returns a random nucleotide from A, C, G, or T.
#############################################################################
def rand_nuc():
    return random.choice( ['A', 'C', 'T', 'G'] )



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
