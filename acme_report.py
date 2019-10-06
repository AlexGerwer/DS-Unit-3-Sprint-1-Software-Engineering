"""
Acme Products
"""
import random
import unittest


class Product(object):
    # class of all products
    def __init__(self, name):
        self.name = name
        # determines product selection
        import itertools
        # self.default defined as 0 when self.name is in product_names
        self.default = 0
        noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Boxing Glove', 'Model']
        adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved', 'Excellent']
        word_pairs = list(itertools.product(adjective, noun))

        max = len(adjective)*len(noun)
        seperator = ' '

        # create list of names
        product_names = []
        index = 0
        for index in range(max):
            product_names.append(seperator.join(word_pairs[index]))
            index = index + 1

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

        # search for self.name in product_names list and preserves its location in the list
        if self.name not in product_names:
            # set default value for when self_name is not in product_names
            self.default = 1
            print ('Product not in inventory, has default values')
        else:
            # provide value specific to product in list
            self.product_selection_number = product_names.index(self.name)

    def price(self):
        # price of product (integer)
        # select price from list
        if self.default == 1:
            # set default value
            price = 10
        else:
            # provide value specific to product in list
            price = self.product_prices[self.product_selection_number]
        return price

    def weight(self):
        # weight of product (interger)
        # select weight from list
        if self.default == 1:
            # set default value
            weight = 20
        else:
            # provide value specific to product in list
            weight = self.product_weights[self.product_selection_number]
        return weight

    def flammability(self):
        # flammability of product (float)
        # select flamability from list
        if self.default == 1:
            # set default value
            flammability = 0.5
        else:
            # provide value specific to product in list
            flamability = self.product_flamabilities[self.product_selection_number]
        return flamability

    def identifier(self):
        # identifier of product (integer: 1000000 - 9999999)
        # select identifier from list
        if self.default == 1:
            # set default value
            identifier = 0000000
        else:
            # provide value specific to product in list
            identifier = self.product_identifiers[self.product_selection_number]
        return identifier

    def stealability(self):
        # defined as price divided by weight; delivers message based upon value
        stealability = self.price/self.weight
        if (stealability < 0.5):
            print('Not so stealable')
        elif (stealability < 1.0):
            print('Kinda stealable')
        else:
            print('Very stealable')
        return

    def explode(self):
        """
        defined as as the flammability times the weight; delivers message based
        upon value
        """
        explode = self.flammability*self.weight
        if (explode < 10):
            print ('...fizzle')
        elif (explode < 50):
            print('...boom')
        else:
            print('...BABOOM!!')
        return


class BoxingGlove(Product):
    """
    The class of a particular product, boxing glove
    # https://stackoverflow.com/questions/41623464/change-default-constructor-argument-value-inherited-from-parent-class-in-subcl
    """

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super(BoxingGlove, self).__init__(name=name, price=price, weight=weight, flammability=flammability)

    def explode(self):
        # re-defined for BoxingGlove
        print('...its a glove')
        return

    def punch(self):
        # provides message based upon weight
        if (self.weight < 5):
            print ('That tickles.')
        elif (self.weight < 15):
            print('Hey that hurt!')
        else:
            print('OUCH!')
            return
