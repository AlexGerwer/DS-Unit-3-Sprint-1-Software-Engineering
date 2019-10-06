"""
Acme Products
"""
import random
import unittest

class Product(object):
    #class of all products
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name=name
        self.price=price
        self.weight=weight
        self.flammability=flammability

    def name(self):
        #name of product
        self.name=self.name
        return self.name

    def price(self):
        #price of product (integer)
        pass

    def weight(self):
        #weight of product (interger)
        pass

    def flammability(self):
        #flammability of product (float)
        pass

    def identifier(self):
        #identifier of product (integer: 1000000 - 9999999)
        identifier=random.randint(1000000, 9999999)
        print (identifier)
        return

    def stealability(self):
        #defined as price divided by weight; delivers message based upon value
        stealability = self.price/self.weight
        if (stealability<0.5):
            print('Not so stealable')
        elif (stealability<1.0):
            print('Kinda stealable')
        else:
            print('Very stealable')
        return

    def explode (self):
        #defined as as the flammability times the weight; delivers message based upon value
        explode = self.flammability*self.weight
        if (explode<10):
            print ('...fizzle')
        elif (explode<50):
            print('...boom')
        else:
            print('...BABOOM!!')
        return

class BoxingGlove(Product):
    """
    The class of a particular product, boxing glove
    # https://stackoverflow.com/questions/41623464/change-default-constructor-argument-value-inherited-from-parent-class-in-subcl
    """

    def __init__(self, name, price=10, weight = 10, flammability = 0.5):
        super(BoxingGlove, self).__init__(name = name, price = price, weight= weight, flammability=flammability)

    def explode (self):
        #re-defined for BoxingGlove
        print('...its a glove')
        return

    def punch(self):
        #provides message based upon weight
        if (self.weight<5):
            print ('That tickles.')
        elif (self.weight<15):
            print('Hey that hurt!')
        else:
            print('OUCH!')
            return
