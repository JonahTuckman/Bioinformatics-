import pandas as pd
# Using pandas to read the data because it is great

# reading the file
data = pd.read_csv('data.csv', header = None)
 

# helper function to get the at content
# Pretty self explanatory, no more contents needed
def at_getter(data):
    num_a = data.upper().count('A')
    num_t = data.upper().count('T')
    at_content = (num_a + num_t) / len(data)
    return at_content
    

# iterating over the different rows so that I can check the name
for index, row in data.iterrows():
    # checking conditions
    if at_getter(row[1]) < 0.5 and row[3] > 200:
        print(row[2])
