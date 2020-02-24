import pandas as pd
# Using pandas to read the data because it is great

# reading the file
data = pd.read_csv('data.csv', header = None)


# iterating over the different rows so that I can check the conditions
for index, row in data.iterrows():
    # checking conditions
    if (row[2].startswith('k') or row[2].startswith('h')) and row[1] != 'Drosophila melanogaster':
        print(row[2])
