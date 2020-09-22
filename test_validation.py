import unittest
from input_validation import validation


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with self.assertRaises(ValueError):
            validation.average(-90,80,70)

    def test_another(self):
        with self.assertRaises(ValueError):
            validation.average(90,-80,70)

    def test_third(self):
        with self.assertRaises(ValueError):
            validation.average(90,80,-70)


if __name__ == '__main__':
    unittest.main()
