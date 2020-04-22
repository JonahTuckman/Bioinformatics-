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

count = 0 #counter to be used to set alignemnts
for line in blast_file:

    # Below I have written a state machine which travels through states using the 'state' variable as the state tracker
    # Each conditional will change the state to its appropraite response and then the looping will continue its checks
    # The regex uses the form of  '^.* WORDS *$' to check for matching lines
    
    # if we're looking for the new Query= line...
    if state == S1:
        match = re.search(r'^Query=\s+([\w\.]+)', line)
        if match:
            current_EST = match.group(1)
            #print(current_EST) # print here for now
            state = S2         # no other states to transition to yet
            
    elif state == S2:
        #print("state2")
        match = re.search(r'\s+[(]([\w\.]+[,]?[^\s]+)\s+([\w\.]+)[)]', line)
        if match:
            length = match.group(1)
            state = S3
   
    elif state == S3:
        #print("state3")
    # Here is the issue, with the regex in state 3
    # Error is here, only one match throughout the whole thing
    # This error is why conditional isnt workign below
        match = re.search(r'Query:\s+(([\w\.])+)\s+([\w\.])', line)
        if match:
            query = match.group(1)
            m_lett = match.group(3)
            print(m_lett)
            state = S4
            count = 1
                
        match_nohits = re.search(r'[*]+\s+No\s+hits\s+found\s+[*]+', line)
        if match_nohits:
            state = S1
           
    # We need to print in state 4 solely
    elif state == S4:
        #print("state4")
        # I am getting into state4, there is an error here
        match = re.search(r'Sbjct:\s+(([\w\.])+)\s+([\w\.])', line)
        count += 1

        if match and count == 3:
            #print("check")
            # We are getting here so the error is in the check below
            first = match.group(1)
            second = match.group(3)
            #print(second)
            
            # error is somewhere in this check
            if m_lett == "M" and second == "M":
            # Not printing anything so I would expect that the error is somewhere in this area
            # Not getting here ever
                #print("done")
                print("%s %d %s" % (current_EST, length, query))
                state = S1
                
        match_first_al = re.search(r'(BLASTX 2.2.21)', line)
        elif match_first_al:
            state = S1
    # add elif's for the missing states, one at a time
    # advice: add the missing states in order - S2, S3, S4

    else:
        print("===> Error processing BLAST output: this line shouldn't print")

blast_file.close()
