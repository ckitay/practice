

from typing import List
from unittest import TestCase


class Test(TestCase):
    def test1(self):
        self.assertEqual(placeholder(), [0])

    def test2(self):
        self.assertEqual(placeholder(), [1])

    def test3(self):
        self.assertEqual(placeholder(), [2])


def placeholder() -> List[int]:
    return [0]
