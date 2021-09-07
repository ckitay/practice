# Given an array of integers and a value, determine if there are any two integers
# in the array whose sum is equal to the given value.
# Return true if the sum exists and return false if it does not.
# https://www.educative.io/blog/crack-amazon-coding-interview-questions

from typing import List
from unittest import TestCase


class Test(TestCase):
    # 7+3=10, 2+8=10
    def test1(self):
        self.assertTrue(find_sum_of_two(nums=[5, 7, 1, 2, 8, 4, 3], target=10))

    # No 2 values sum up to 19
    def test2(self):
        self.assertFalse(find_sum_of_two(nums=[5, 7, 1, 2, 8, 4, 3], target=19))

    # 1 + 2 = 3
    def test3(self):
        self.assertTrue(find_sum_of_two(nums=[5, 7, 1, 2, 8, 4, 3], target=3))

    # No 2 values sum up to 4, this is an assumption, requirement clarification may be needed?
    def test4(self):
        self.assertFalse(find_sum_of_two(nums=[4, 2, 1, 5], target=4))

    # At least 2 values are always needed, this is an assumption, requirement clarification may be needed?
    def test5(self):
        self.assertFalse(find_sum_of_two(nums=[1], target=1))

    # -5+1=4
    def test6(self):
        self.assertTrue(find_sum_of_two(nums=[-5, -99, 0, 1, 3], target=4))

    # No 2 values sum up to 2
    def test7(self):
        self.assertFalse(find_sum_of_two(nums=[-5, -99, 0, 1, 3], target=2))

    # 2+2=4
    def test8(self):
        self.assertFalse(find_sum_of_two(nums=[2, 2], target=4))


def find_sum_of_two(nums: List[int], target: int) -> bool:
    # Scan the whole array once and store visited elements in a hash set.
    hash_visited = set(nums)

    # During scan, for every element e in the array, we check if
    # val - e is present in the hash set i.e. val - e is already visited.
    for num in nums:
        # If val - e is found in the hash set,
        pair_1 = target - num
        if hash_visited.issuperset({pair_1}):

            pair_2 = target - pair_1
            is_duplicate = pair_1 == pair_2

            # Doesn't count if it already exists unless it's a duplicate
            if not is_duplicate:
                return True

        # If we have exhausted all elements in the array and
        hash_visited.add(num)

    # did not find any such pair, the function will return false
    return False
