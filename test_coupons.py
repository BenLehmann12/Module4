import unittest
from Score import coupon_calculation as calc


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(calc.calculate_price(10, 5, 10), calc.calculate_price(10, 5, 10))

    def test_second(self):
        self.assertEqual(calc.calculate_price(15, 5, 10), calc.calculate_price(15, 5, 10))

    def test_third(self):
        self.assertEqual(calc.calculate_price(45, 5, 10), calc.calculate_price(45, 5, 10))

    def test_fourth(self):
        self.assertEqual(calc.calculate_price(55,5,10), calc.calculate_price(55,5,10))






if __name__ == '__main__':
    unittest.main()
