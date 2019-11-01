"""
Acme Products
"""
import random
import unittest


class Product(object):
    """
    class of all products
    """
    def __init__(self, name, price=10, weight=20, flamability=0.5):
        self.name = name

        # self.default defined as 0 when self.name is in product_names
        self.default = 0

        # Make list of products from List of adjective and noun choices
        self.noun = [' Anvil', ' Catapult', ' Disguise', ' Mousetrap',
                     ' Boxing Glove', ' Model']
        self.adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable',
                          'Improved', 'Excellent']
        # Length of list of all possible adjective and noun combinations
        max = len(self.adjective)*len(self.noun)
        # Combine none and adjective lists
        output = self.adjective + self.noun +\
            [item_one+item_two\
            for item_one in self.adjective for item_two in self.noun]
        # Drop first 12 items in list
        # which are individual items from original list
        products = output[12:]
        self.product_names = products

        # create list of prices
        self.product_prices = []
        index = 0
        for index in range(max):
            self.product_prices.append(random.randint(5, 100))
            index = index + 1

        # create list of weights
        self.product_weights = []
        index = 0
        for index in range(max):
            self.product_weights.append(random.randint(5, 100))
            index = index + 1

        # create list of flamabilities
        self.product_flamabilities = []
        index = 0
        # max = len(adjective)*len(noun)
        for index in range(max):
            self.product_flamabilities.append(random.uniform(0.0, 2.5))
            index = index + 1

        # create list of identifiers
        self.product_identifiers = []
        index = 0
        # max = len(adjective)*len(noun)
        for index in range(max):
            self.product_identifiers.append(random.randint(1000000, 9999999))
            index = index + 1

        # search for self.name in product_names list
        # and preserves its location in the list
        if self.name not in products:
            # set default value for when self_name is not in product_names
            self.default = 1
            print ('Product not in inventory, has default values')
        else:
            # provide value specific to product in list
            print ('Product is in inventory')
            self.product_selection_number = products.index(self.name)

        # price of product (integer)
        # select price from list
        if self.default == 1:
            # set default value
            self.price = 10
        else:
            # provide value specific to product in list
            self.price = self.product_prices[self.product_selection_number]

        # weight of product (interger)
        # select weight from list
        if self.default == 1:
            # set default value
            self.weight = 20
        else:
            # provide value specific to product in list
            self.weight = self.product_weights[self.product_selection_number]

        # flammability of product (float)
        # select flamability from list
        if self.default == 1:
            # set default value
            self.flamability = 0.5
        else:
            # provide value specific to product in list
            self.flamability = self.product_flamabilities[
                self.product_selection_number]

        # identifier of product (integer: 1000000 - 9999999)
        # select identifier from list
        if self.default == 1:
            # set default value
            self.identifier = 0000000
        else:
            # provide value specific to product in list
            self.identifier = self.product_identifiers[
                self.product_selection_number]

    def stealability(self):
        # defined as price divided by weight; delivers message based upon value
        stealability = self.price/self.weight
        if (stealability < 0.5):
            return 'Not so stealable.'
        elif (stealability < 1.0):
            return 'Kinda stealable.'
        else:
            return 'Very stealable.'

    def explode(self):
        # defined as as the flamability times the weight;
        # delivers message based upon value
        explode = self.flamability*self.weight
        if (explode < 10):
            return '...fizzle.'
        elif (explode < 50):
            return '...boom!'
        else:
            return '...BABOOM!!'

    def inventory_report(self):
        # create a dataframe with columns taken from the following lists
        # self.product_names
        # self.product_prices
        # self.product_weights
        # self.product_flamabilities
        import pandas as pd

        # Initial Inputs
        items = len(self.product_names)
        index = self.product_names
        columns = ['product price', 'product weight', 'product flamability']

        # Create empty data frame with labels
        acme_official_inventory_report = pd.DataFrame(index=index,
                                                      columns=columns)
        acme_official_inventory_report =\
            acme_official_inventory_report.fillna(0)

        # Fill data frame
        index = 0
        for index in range(items):
            acme_official_inventory_report.iloc[index, 0] =\
                self.product_prices[index]
            acme_official_inventory_report.iloc[index, 1] =\
                self.product_weights[index]
            acme_official_inventory_report.iloc[index, 2] =\
                self.product_flamabilities[index]
            index = index + 1

        # Add mean values
        acme_official_inventory_report.loc['AVERAGE'] =\
            acme_official_inventory_report.mean()

        # Create table
        acme_official_inventory_report.head(37)
        print (acme_official_inventory_report.head(37), '\n')

        # Create summary
        return print ('ACME CORPORATION OFFICIAL INVENTORY REPORT', '\n',
                     'Unique product names: ', items, '\n',
                     'Average price: ',
                     acme_official_inventory_report.iloc[36, 0], '\n',
                     'Average weight: ',
                     acme_official_inventory_report.iloc[36, 1], '\n',
                     'Average flammability: ',
                     acme_official_inventory_report.iloc[36, 2])

    if __name__ == '__main__':
        inventory_report


class BoxingGlove(Product):
    """
    The class of a particular product, boxing glove
    """
    def __init__(self, name, price=10, weight=10, flamability=0.5):
        super(BoxingGlove, self).__init__(name=name, price=price,
                                          weight=weight,
                                          flamability=flamability)

    def explode(self):
        # re-defined for BoxingGlove, independent of flamability and weight
        print("'...it's a glove.'")
        return

    def punch(self):
        # provides re defined message based upon weight
        if (self.weight < 5):
            print ("'That tickles.'")
        elif (self.weight < 15):
            print("'Hey that hurt!'")
        else:
            print("'OUCH!'")
        return
