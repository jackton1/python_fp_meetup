from unittest import TestCase

num = 2


class TestMultiplyTwoNums(TestCase):
    def test_multiply_two_nums(self):
        self.assertTrue(isinstance(num, int))

    def test_equal_nums(self):
        self.assertEqual(num, 2)

