from __future__ import division
from random import seed
from random import randint

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')

c_count = my_dna.count('C')
g_count = my_dna.count('G')

at_content = (a_count + t_count) / length
cg_content = (c_count + g_count) / length
print("AT content is " + str(at_content))
print("CG count is " + str(cg_content))
combined = at_content + cg_content
#print("%d should be 1, otherwise error" % combined)

#Error Check
if combined != 1:
    print("FAIL ... Some not counted ?!?!?!?")
else:
    print("SUCCESS ... All accounted for")

#Random DNA creation
#Seed random
seed(1)

ACTG = ['A','C','T','G']
empty_word = ""
for i in range(0, length):
    rand_num = randint(0, 3)
    empty_word = empty_word + ACTG[rand_num]
print("Random string of DNA: %s " % empty_word)
