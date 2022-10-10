import unittest
from mtg_manabase_builder import manabase_builder as mb


class MTGManabaseBuilderTestCase(unittest.TestCase):

    def setUp(self):
        self.MB = mb.MTGManabaseBuilder(60)

'''
    def test_integer_number(self):
        """Test """

        # -7 multiplied by 2 return -14
        result = self.multiplication.multiply(-7)
        self.assertEqual(result, -14)
'''
if __name__ == '__main__':
    unittest.main()