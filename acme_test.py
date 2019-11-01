import unittest
from acme_report import Product


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flamability(self):
        """Test default product flamability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flamability, 0.5)

    def test_default_product_stealability(self):
        """Test default product stealability being 'Kinda Stealable.'."""
        prod = Product('Test Product')
        stealability_test = prod.stealability()
        stealability_correct = 'Kinda stealable.'
        self.assertMultiLineEqual(stealability_test, stealability_correct)

    def test_specific_product_stealability(self):
        """Test default product stealability"""
        prod = Product('Improved Catapult')
        stealability_test = prod.stealability()
        stealability = prod.price/prod.weight
        if (stealability < 0.5):
            stealability_correct = 'Not so stealable.'
        elif (stealability < 1.0):
            stealability_correct = 'Kinda stealable.'
        else:
            stealability_correct = 'Very stealable.'
        self.assertMultiLineEqual(stealability_test, stealability_correct)

    def test_default_product_explode(self):
        """Test default product explode being '...boom!'."""
        prod = Product('Test Product')
        explode_test = prod.explode()
        explode_correct = '...boom!'
        self.assertMultiLineEqual(explode_test, explode_correct)

    def test_specific_product_explode(self):
        """Test specific product explode"""
        prod = Product('Awesome Anvil')
        explode_test = prod.explode()
        explode = prod.flamability*prod.weight
        if (explode < 10):
            explode_correct = '...fizzle.'
        elif (explode < 50):
            explode_correct = '...boom!'
        else:
            explode_correct = '...BABOOM!!'
        self.assertMultiLineEqual(explode_test, explode_correct)

class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""
    # _Product__member
    def test_default_num_products(self):
        """Output receives a list of length 36."""
        prod = Product('Test Product')
        product_names_list_length = len(prod.product_names)
        self.assertEqual(product_names_list_length, 36)

    def test_legal_names(self):
        """
        Check that the generated names for a default batch of products are all
        valid possible names to generate
        """
        # Make list of products from List of adjective and noun choices
        # Length of list of all possible adjective and noun combinations
        prod = Product ('Test Product')
        max = len(prod.adjective)*len(prod.noun)
        # Combine none and adjective lists
        output = prod.adjective + prod.noun +\
            [item_one+item_two\
            for item_one in prod.adjective for item_two in prod.noun]
        # Drop first 12 items in list
        # which are individual items from original list
        legal_names = output[12:]

        # test product_names against legal_names
        # max = len(adjective)*len(noun)
        mindex = 0
        for mindex in range(max):
            product_names_test = prod.product_names[mindex]
            product_names_correct = legal_names[mindex]
            self.assertIn(product_names_test, product_names_correct)
            mindex = mindex + 1

if __name__ == '__main__':
    unittest.main()
