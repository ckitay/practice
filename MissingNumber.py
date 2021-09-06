# All numbers from 1 to n are present except one number x. Find x
# https://www.educative.io/blog/crack-amazon-coding-interview-questions

# n = expected_length

# Test Case 1 , Expect = 6
from typing import List
from unittest import TestCase


class Test(TestCase):
    def test1(self):
        self.assertEqual(find_missing_number([3, 7, 1, 2, 8, 4, 5], 8), 6)

    def test2(self):
        self.assertEqual(find_missing_number([3, 1], 3), 2)

    def test3(self):
        self.assertEqual(find_missing_number([2], 2), 1)


def find_missing_number(nums: List[int], expected_length: int) -> List[int]:
    # Find sum of all values in nums
    sum_nums = sum(nums)

    # Created expectedNums, starting with 1 and ending with expected_length
    expected_nums = range(1, expected_length + 1)

    # Find sum of all expectedNums values
    sum_expected = sum(expected_nums)

    # Return Missing number
    return sum_expected - sum_nums
