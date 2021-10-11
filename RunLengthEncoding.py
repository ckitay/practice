

from typing import List
from unittest import TestCase


class Test(TestCase):
    def test1(self):
        self.assertEqual(
            "2a1b2c1a",
            encode("aabcca")
        )


def encode(input: "") -> "":
    # Check for null input
    if input is None or len(input) == 0:
        return ""

    prevChar = 0
    counter = 0
    newString = ""

    for char in input:
        if char == prevChar:
            counter += 1
        else:
            if prevChar != 0:
                newString += str(counter)
                newString += prevChar
            prevChar = char
            counter = 1

    # Append the last one
    newString += str(counter)
    newString += prevChar

    return newString