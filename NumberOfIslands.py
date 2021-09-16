# https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/894/
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.

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

        self.assertEqual(1, Solution.numIslands(self, grid))

    def test2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]

        self.assertEqual(3, Solution.numIslands(self, grid))

    def test3(self):
        grid = [
            ["1"]
        ]

        self.assertEqual(1, Solution.numIslands(self, grid))

    def test4(self):
        grid = [
            ["1"],
            ["1"],
            ["1"]
        ]

        self.assertEqual(1, Solution.numIslands(self, grid))

    def test5(self):
        grid = [
            ["1", "0", "1"],
            ["1", "0", "1"],
            ["1", "0", "0"]
        ]

        self.assertEqual(2, Solution.numIslands(self, grid))


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        # 0 = water
        # 1 = land
        # 2 = already counted as being part of an island

        island_count = 0
        row_count = len(grid)

        # ToDo Add unit tests and validate input values are valid
        # May consider using this? https://stackoverflow.com/questions/3248851/pythons-enum-equivalent

        # ToDo Add unit and Verify the grid is a square?
        col_count = len(grid[0])

        # Iterate through m
        latitude = 0
        for lane in grid:

            # do a DFS Depth First Search on each tile
            longitude = 0
            for tile in lane:

                # If tile is land and # don't count the islands we already visited
                if Solution.is_land(tile) and not Solution.is_island_visited(tile):

                    # We know there is new island here
                    island_count += 1

                    # Mark all connected land as island that we already visisted
                    Solution.dfs_visit_all_tiles_in_island(grid, latitude, longitude)

                longitude += 1

            latitude += 1
        return island_count

    # Now lets use DFS recursion to visit all the horizontal and vertical tiles so
    # that we can mark them as counted
    def dfs_visit_all_tiles_in_island(grid: List[List[str]], latitude: int, longitude: int):

        tile = grid[latitude][longitude]

        # We don't want to keep re-visiting the same tiles
        if not Solution.is_island_visited(tile):

            # Hurray! We are now visiting tile on this island and marking it by sticking a flag in it or something.
            grid[latitude][longitude] = "2"

            # Now let's see if we can visit the south tile and do this all over again
            Solution.south_tile(grid, latitude, longitude)

            # Now let's see if we can visit the south tile and do this all over again
            Solution.east_tile(grid, latitude, longitude)

        # Mark all adjacent horizontal land values as already counted as being part of an island

        # Mark all adjacent vertical land values as already counted as being part of an island

        return grid

    def is_land(tile: str) -> bool:
        if tile == 1:
            return True
        elif tile == "1":
            return True
        else:
            return False

    def is_island_visited(tile: str) -> bool:
        if tile == 2:
            return True
        elif tile == "2":
            return True
        #elif Solution.is_water_look(tile):
            #return True
        else:
            return False

    def is_water(self: str) -> bool:
        if self == 0:
            return True
        elif self == "0":
            return True
        else:
            return False

    def is_water_look(self: List[List[str]], latitude: int, longitude: int) -> bool:
        try:
            tile = self[latitude][longitude]

            # This should sometimes be water or sometimes be land
            return Solution.is_water(tile)
        except IndexError:
            # Todo, Check if out of bounds instead of using try
            return True  # Outside the grid is water

    def south_tile(self: List[List[str]], latitude: int, longitude: int):

        # We cannot be visiting water!
        if not Solution.is_water_look(self, latitude + 1, longitude):
            Solution.dfs_visit_all_tiles_in_island(self, latitude + 1, longitude)

    def east_tile(self: List[List[str]], latitude: int, longitude: int):

        # We cannot be visiting water!
        if not Solution.is_water_look(self, latitude, longitude + 1):
            Solution.dfs_visit_all_tiles_in_island(self, latitude, longitude + 1)
