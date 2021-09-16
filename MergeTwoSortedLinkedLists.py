# Given two sorted linked lists,
# merge them so that the resulting linked list is also sorted.
# Consider two sorted linked lists and the merged list below them as an example.
from typing import List
from unittest import TestCase

from requests import head


class Test(TestCase):
    def test1(self):
        actual = test_list(merged_sorted([4, 8, 15, 19], [7, 9, 10, 16]))
        expected = [4, 7, 8, 9, 10, 15, 16, 19]
        self.assertEqual(
            expected,
            actual
        ),

    # What if head1, head2 aren't fed in sequence?
    def test2(self):
        self.assertEqual(
            test_list(merged_sorted([8, 4, 15, 19], [9, 7, 10, 16])),
            [4, 7, 8, 9, 10, 15, 16, 19]
        ),

    def test3(self):
        self.assertEqual(
            merged_sorted([], [0]),
            [0]
        ),

    def test4(self):
        self.assertEqual(
            merged_sorted([1], [1]),
            [1, 1]
        ),

    def test5(self):
        self.assertEqual(
            merged_sorted([-1], [3, 2]),
            [-1, 2, 3]
        ),


# Check the whole list for unit testing purposes
def test_list(self) -> List[int]:
    nums = []

    current = self.head
    while current:
        nums.append(current.data)
        current = current.next

    return nums


def merged_sorted(head1: head, head2: head) -> head:
    merge = LinkedList()

    for num1 in head1:
        if len(head2) > 0:
            num2 = head2.pop(0)
            # Choose the head of the merge by comparing 1st node of both linked lists
            if num2 > num1:
                merge.insert(num1)
                merge.insert(num2)
            else:
                merge.insert(num2)
                merge.insert(num1)

    # For subsequent nodes, choose smaller node and link to merged tail
    return merge


# https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python
# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

        # print method for the linked list

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
