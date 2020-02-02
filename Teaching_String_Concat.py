## File to show optimal ways to present string Concat

## Bunch of variables
number_1 = 1
number_2 = 2
number_3 = 3
number_4 = 4
strang = "Word"
strung = "Werd"

#####################
# Concat using +
#####################

print("This sentance has the numbers " + str(number_1) + str(number_2) + str(number_3) + str(number_4) + " as well as some words like " + strang + " and " + strung)

# This is not best as you can see the need to type cast 4 different ints as well as continue to use the + sign over and over

#####################
# Using % signs
#####################

print("This sentance has the numbers %d%d%d%d as well as some words like %s and %s" % (number_1, number_2, number_3, number_4, strang, strung))

# This is much cleaner as you can write out your sentance without interuption and not have to worry about the interuptions and can organize all of your variables together at the end
# Also better to avoid bugs as the + signs can become tricky to keep track of and it would be easy to forget to convert the type of a variable to a string 
