import pandas as pd
# Using pandas to read the data because it is great

# reading the file
data = pd.read_csv('data.csv', header = None)

# helper function to get the at content
# Pretty self explanatory, no more contents needed
# Same at helper from the at_content file
def at_getter(data):
    num_a = data.upper().count('A')
    num_t = data.upper().count('T')
    at_content = (num_a + num_t) / len(data)
    return at_content
    

 
# iterating over the different rows so that I can check the name
for index, row in data.iterrows():
    if at_getter(row[1]) > 0.65:
        print("%s has a HIGH AT content" % row[2])
    elif at_getter(row[1]) < 0.45:
        print("%s has a LOW AT content" % row[2])
    else:
        print("%s has a MEDIUM AT content" % row[2])
