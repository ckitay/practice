# https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/894/
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

from typing import List
from unittest import TestCase


class Test(TestCase):

    def test1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]

        self.assertEqual(1, Solution.num_islands(grid))

    def test2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]

        self.assertEqual(1, Solution.num_islands(grid))

    def test3(self):
        grid = [
            [1]
        ]

        self.assertEqual(1, Solution.num_islands(self, grid))


class Solution:

    def num_islands(self, grid: List[List[int]]) -> int:
        # 0 = water
        # 1 = land
        # 2 = already counted as being part of an island

        island_count = 0

        # Iterate through m
        i = 0
        for lane in grid:

            # Iterate through n
            j = 0
            for tile in lane:

                # If tile is land
                if Solution.is_land(tile):

                    # Ignore grid value (tile) if it's already counted as being part of an island

                    # Mark all adjacent horizontal land values as already counted as being part of an island

                    # Mark all adjacent vertical land values as already counted as being part of an island

                    # If East and South are both water
                    if Solution.is_water(Solution.east_tile(grid, i, j)) and Solution.is_water(
                            Solution.south_tile(grid, i, j)):
                        # Increment island count
                        island_count += 1

                j += 1

            i += 1
        return island_count

    # def island_row(lane: List[int])

    def south_tile(grid: List[List[int]], i: int, j: int) -> int:
        # Todo, Check if out of bounds instead of using try
        m = len(grid) - 1

        try:
            return grid[i + 1][j]
        except IndexError:
            return 0  # Outside the grid is water

    def east_tile(grid: List[List[int]], i: int, j: int) -> int:
        # Todo, Check if out of bounds instead of using try
        n = len(grid[i]) - 1

        try:
            return grid[i][j + 1]
        except IndexError:
            return 0  # Outside the grid is water

    def is_land(tile: int) -> int:
        if tile == 1:
            return True
        elif tile == "1":
            return True
        else:
            return False

    def is_water(tile: int) -> int:
        if tile == 0:
            return True
        elif tile == "0":
            return True
        else:
            return False
