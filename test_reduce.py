import unittest

from functools import reduce

nums = list(range(1, 10))
states = ['Ohio', 'Alaska', 'California', 'Oklahoma']


class TestReduceFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_nums, sum(nums))

    def test_multiply_numbers(self):
        self.assertEqual(multiply_nums, 362880)

    def test_longest_string(self):
        self.assertEqual(longest_string, 'California')

add_nums = reduce(lambda x, y: x + y, nums)
multiply_nums = reduce(lambda x, y: x * y, nums)
longest_string = reduce(lambda x, y: x if len(x) > len(y) else y, states)

if __name__ == '__main__':
    unittest.main()
