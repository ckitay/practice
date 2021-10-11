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

    # 21 seconds memory error
    def test6(self):
        m = 0
        n = 0

        row_one = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        water_row = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        grid = [row_one, water_row]

        # n = 300 hard-coded
        row_repeat = ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]

        while m <= 300:
            grid.append(row_repeat)
            m += 1

        self.assertEqual(4, Solution.numIslands(self, grid))


class Solution:
    # Big O Notation Performance metric?. E.g. if n=300 or grid limit size is 300 x 300
    # then we shouldn't be visiting more than 300 x 300 tiles?
    # ToDo: Create a stress this so tiles_visit_count gets hit nearly 90,000 times?
    tiles_visted_count = 0

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

                    # Mark all connected land as island that we already visited
                    Solution.dfs_visit_all_tiles_in_island(grid, latitude, longitude)

                longitude += 1

            latitude += 1

        print('Tiles visited: ' + str(Solution.tiles_visted_count))

        return island_count

    # Now lets use DFS recursion to visit all the horizontal and vertical tiles so
    # that we can mark them as counted
    def dfs_visit_all_tiles_in_island(self: List[List[str]], latitude: int, longitude: int):

        tile = self[latitude][longitude]

        # We don't want to keep re-visiting the same tiles
        if not Solution.is_island_visited(tile):
            # Hurray! We are now visiting tile on this island and marking it by sticking a flag in it or something.
            self[latitude][longitude] = "2"

            Solution.tiles_visted_count += 1

            # Now let's see if we can visit the south tile and do this all over again
            Solution.south_tile(self, latitude, longitude)

            # Now let's see if we can visit the east tile and do this all over again
            Solution.east_tile(self, latitude, longitude)

        return self

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
        # elif Solution.is_water_look(tile):
        # return True
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
