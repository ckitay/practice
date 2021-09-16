

from typing import List
from unittest import TestCase


class Test(TestCase):
    def test1(self):
        self.assertEqual(
            0,
            placeholder({0,0,0}, 0)
        )

    def test2(self):
        self.assertEqual(
            1,
            placeholder({0, 0, 0}, 0)
        )

    def test3(self):
        self.assertEqual(
            2,
            placeholder({0, 0, 0}, 0)
        )


def placeholder(nums: List[int], value: int) -> int:
    return 0
