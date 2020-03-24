#--------------------------------------------------------------------
#
# BIOL / CMPU 353
# Spring 2020
#
# BLAST Parse Assignment
#
# Algorithm by: Jodi Schwarz and Marc Smith
# Written by: Marc Smith
#
# Description: Extract matches from results of BLAST search
#              that begin with ATG.
#
#--------------------------------------------------------------------

import re

#----------------------------------------------------------------
# FSM: Finite State Machine (has states and transitions)
# - states: each state represents the line being searched for in
#           the BLAST search results file.
# - transitions: describe how the FSM changes from one state to
#                another.
#
# There will be four possible states in our FSM, upon completion
# of this project: S1-S4
# Note: this initial version uses only one state
#
# Here is what each state represents:
#
# S1: looking for "Query="
# S2: looking for "(nnn letters)"
# S3: looking for "Query:" or "No hits found"
# S4: looking for "Sbjct: nnn"
#
# Here is a table representation of the state transition function
# with initial state S1. (this is equivalent to drawing a state
# transition diagram, which is hard to do in a text file)
#
# From-State  To-State  if Line match =
# ----------  --------  ---------------
#     S1         S2     "Query="
#     S2         S3     "(nnn letters)"
#     S3         S1     "No hits found"
#     S3         S4     "Query:
#     S4         S1     "Sbjct:"
#----------------------------------------------------------------

# initialize states S1 - S4, and start state
S1 = 1
S2 = 2
S3 = 3
S4 = 4
state = S1

# Print header line
print("EST\tEST Length\tQuery Start Position")
   
blast_file_name = "/home/joschwarz/public/blast/AipTransc_v_SwissProt.blastx"
blast_file = open(blast_file_name, 'r')

for line in blast_file:

    # if we're looking for the new Query= line...
    if state == S1:
        match = re.search(r'^Query=\s+([\w\.]+)', line)
        if match:
            current_EST = match.group(1)
            print(current_EST) # print here for now
            state = S1         # no other states to transition to yet
    
    # add elif's for the missing states, one at a time
    # advice: add the missing states in order - S2, S3, S4

    else:
        print("===> Error processing BLAST output: this line shouldn't print")

blast_file.close()
