import pandas as pd
# Using pandas to read the data because it is great

# reading the file
data = pd.read_csv('data.csv', header = None)
 

# itterating over the different rows so that I can check the name
for index, row in data.iterrows():
    # conditional check
    if row[0] == 'Drosophila melanogaster' or row[0] == 'Drosophila simulans':
        # If passed then print it
        print(row[1])

# This is lazy code, I should rename the rows rather than using the default 1 and 0 but this gets the job done and does not need to be clean / reusable
