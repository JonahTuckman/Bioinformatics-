import pandas as pd
# Using pandas to read the data because it is great

# reading the file
data = pd.read_csv('data.csv', header = None)
 
# iterating over the different rows so that I can check the length of the gene names
for index, row in data.iterrows():
    # conditional check
    # The data is unlabelled so I am assuming that this is what is intended
    if len(row[1]) >= 90 and len(row[1]) <= 110:
        print(row[1])
        
# Similarly to several_species, lazy code
