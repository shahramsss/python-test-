import unittest
from person import Person


class PersonTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Person('sss', 'shah')
        self.p2 = Person('s2', 'sh2')

    def tearDown(self):
        print('Done ...')

    def test_fullname(self):
        self.assertEqual(self.p1.fullname(), 'sss shah')
        self.assertEqual(self.p2.fullname(), 's2 sh2')

    def test_email(self):
        self.assertEqual(self.p1.email(), 'sss@gmail.com')
        self.assertEqual(self.p2.email(), 's2@gmail.com')


if __name__ == '__main__':
    unittest.main()
