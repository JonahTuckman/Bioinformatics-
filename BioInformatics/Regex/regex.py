#BIOL/CMPU-377
# Spring 2020
# Project 3 Regex
# DNA: Playing with Strings
# Author: Jonah Tuckman
#-----------------------------------------------------------------
import re
#
# Summary: This Python program isolates the upstream and genic
# regions of a sequence. A report is printed, a sample
# of which is saved in file: genic-report.txt
#
# This time doing the work using the re (regex) package 
#
# Run Command:  python Upstream_v_Genetic.py > genic-report.txt
#
#-----------------------------------------------------------------
print("\n+++++++++ Upstream and Genic Report ++++++++++++++++\n")

# upstream and start of a gene ...
some_sequence = "cgccatataatgctcgtccgcgcccta"
print("Starting sequence is: %s " % some_sequence)

# convert all nucleotides to uppercase
some_sequence = some_sequence.upper() 
print("Converted to uppercase: %s " % some_sequence)

# get the length of sequence
seq_length = len(some_sequence)
print("Length of starting sequence is: %d" % seq_length)
print("\n---------------------------------------------\n")

# get the position of the start codon &quot;ATG&quot; and the next two codons
match = re.search('ATG', some_sequence).start()
print("ATG start codon begins in position (bp) %d " % (match+1))
codon_2_pos = match + 3
codon_2 = some_sequence[codon_2_pos:codon_2_pos+3]
print("\tfollowed by %s in position (bp) %d" % (codon_2, (codon_2_pos+1)))
codon_3_pos = codon_2_pos + 3
codon_3 = some_sequence[codon_3_pos:codon_3_pos+3]
print("\tfollowed by %s in position (bp) %d" % (codon_3, (codon_3_pos+1)))
print("\n----------------------------------------------\n")

# get the upstream and genic sequences
#upstream_seq, ATG, genic_seq = some_sequence.partition("ATG")
# Instead of above code, using re search to find the index and then this index to chop accordingly
upstream_seq = some_sequence[0:match]
ATG = 'ATG'
end_match = re.search('ATG', some_sequence).end()
genic_seq = some_sequence[end_match:]

upstream_len = len(upstream_seq)
print("\n----------------------------------------------\n")
print("Upstream sequence is: %s" % upstream_seq)
# ...
# ...

combined_genic = ATG + genic_seq

print("Gene sequence is: %s" % combined_genic)

print("Codon 1 = %s" % ATG)
print("Codon 2 = %s" % some_sequence[end_match:end_match+3])
print("Codon 3 = %s" % some_sequence[end_match+3:end_match+6])

print("\n----------------------------------------------\n")
print("Upstream length is: %d" % upstream_len)
print("Gene length is: %d" % len(combined_genic))
print("\n----------------------------------------------\n")




print("Gene + Strand: " + combined_genic + "\n")
# Compute the reverse complement sequence
reverse_seq = combined_genic[::-1] # neat trick to reverse a string
# Now swap A&#39;s and T&#39;s, C&#39;s and G&#39;s
# hint #1: convert reverse_seq to lower case, then use
# replace() method to complement nucleotides one at a time.
# hint #2: replace &quot;a&quot;s with &quot;T&quot;s, &quot;t&quot;s with &quot;A&quot;s,
# &quot;c&quot;s with &quot;G&quot;s, and &quot;g&quot;s with &quot;C&quot;s
#
reverse_comp_seq = reverse_seq.lower()
reverse_comp_seq = reverse_comp_seq.replace('a', 'T')
reverse_comp_seq = reverse_comp_seq.replace('t', 'A')
reverse_comp_seq = reverse_comp_seq.replace('c', 'G')
reverse_comp_seq = reverse_comp_seq.replace('g', 'C')

print("Gene - Strand: " + reverse_comp_seq)
print("\n----------------------------------------------------\n")
# Print sequence with ATG highlighted
lower_seq = some_sequence.lower()
highlighted_ATG = lower_seq.replace('atg', 'ATG', 1)
print("Hightlighted ATG sequence: %s" % highlighted_ATG)
# ...
# Compute AT-richness of upstream sequence
number_A = upstream_seq.count('A')
number_T = upstream_seq.count('T')
print("AT-richness:")
print("A: %d" % number_A)
print("T: %d" % number_T)
print("\n----------------------------------------------------\n")
