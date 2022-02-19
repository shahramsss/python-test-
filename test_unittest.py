import unit_test
import unittest


class UnitTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(unit_test.sum(1, 2), 3)
        self.assertEqual(unit_test.sum(-3, 2), -1)

    def test_subtract(self):
        self.assertEqual(unit_test.subtract(3, 2), 1)
        self.assertEqual(unit_test.subtract(3, -2), 5)

    def test_multiply(self):
        self.assertEqual(unit_test.multiply(3, 2), 6)
        self.assertEqual(unit_test.multiply(3, -2), -6)

    def test_divitsion(self):
        self.assertEqual(unit_test.division(6, 2), 3)
        self.assertEqual(unit_test.division(6, -2), -3)
        self.assertRaises(ZeroDivisionError, unit_test.division, 5, 0)


if __name__ == '__main__':
    unittest.main()
