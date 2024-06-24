import unittest

from hello import hello_world, sum_of_two_numbers


class HelloTestCase(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")

    def test_sum(self):
        self.assertEqual(sum_of_two_numbers(1, 2), 3)