import unittest
from add import add


class TestBasic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,2), 4)
    def test_add_big_numbers(self):
        self.assertEqual(add(100,100), 200)
    def test_fail(self):
	self.assertEqual(add(150,100), 210)
	print("Hello"                    +"goodbye")


