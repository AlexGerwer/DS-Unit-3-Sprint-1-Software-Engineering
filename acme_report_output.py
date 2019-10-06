# Create Acme Official Inventory Report
import pandas as pd
import itertools
from acme_report import Product

noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Boxing Glove', 'Model']
adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved', 'Excellent']
word_pairs = list(itertools.product(adjective, noun))

max = len(adjective)*len(noun)
seperator = ' '

# Create list of names
product_names = []
index = 0
for index in range(max):
    product_names.append(seperator.join(word_pairs[index]))
    index = index + 1

# Initial Inputs
items = len(product_names)
index = product_names
columns = ['product identifier', 'price', 'weight', 'flammability']

# Create empty data frame with labels
acme_official_inventory_report = pd.DataFrame(index=index, columns=columns)
acme_official_inventory_report = acme_official_inventory_report.fillna(0)

# Fill data frame
index = 0
for index in range(items):
    prod = Product(product_names[index])
    acme_official_inventory_report.iloc[index, 0] = prod.identifier()
    acme_official_inventory_report.iloc[index, 1] = prod.price()
    acme_official_inventory_report.iloc[index, 2] = prod.weight()
    acme_official_inventory_report.iloc[index, 3] = prod.flammability()
    index = index + 1

# Add mean values
acme_official_inventory_report.loc['average'] = acme_official_inventory_report.mean()

# Create table
acme_official_inventory_report.head(37)
print (acme_official_inventory_report.head(37))
