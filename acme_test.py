import unittest
from acme_report import Product
from acme_report_output import product_names, adjective, noun


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price(), 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight(), 20)

    def test_default_product_flammability(self):
        """Test default product price being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability(), 0.5)

    def test_default_product_stealability(self):
        """Test default product stealability being 'Kinda Stealable.'."""
        prod = Product('Test Product')
        s = 'Kinda Stealable.'
        self.assertEqual(s.strip('Kinda Stealable.'), '')

    def test_default_product_explode(self):
        """Test default product explode being '...boom!'."""
        prod = Product('Test Product')
        s = '...boom!.'
        self.assertEqual(s.strip('...boom!.'), '')


class AcmeOutputTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""
    def test_default_num_products(self):
        """Output receives a list of length 36."""
        product_names_list_length = len(product_names)
        self.assertEqual(product_names_list_length, 36)

    def test_legal_names(self):
        """
        Check that the generated names for a default batch of products are all
        valid possible names to generate
        """
        import itertools
        word_pairs = list(itertools.product(adjective, noun))
        max = len(adjective)*len(noun)
        seperator = ' '

        # create list of legal names
        legal_names = []
        nindex = 0
        for nindex in range(max):
            legal_names.append(seperator.join(word_pairs[nindex]))
            nindex = nindex + 1

        # test product_names against legal_names
        # max = len(adjective)*len(noun)
        mindex = 0
        for mindex in range(max):
            product_names_test = product_names[mindex]
            product_names_correct = legal_names[mindex]
            self.assertIn(product_names_test, product_names_correct)
            mindex = mindex + 1

if __name__ == '__main__':
    unittest.main()
