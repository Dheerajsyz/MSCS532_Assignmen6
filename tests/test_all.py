"""
Unit tests for Assignment 6 implementations
"""
import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from part1_selection.median_of_medians import median_of_medians
from part1_selection.quickselect import randomized_quickselect
from part2_structures.arrays import DynamicArray, Matrix
from part2_structures.stack_queue import ArrayStack, ArrayQueue
from part2_structures.linked_list import SinglyLinkedList
from part2_structures.tree import RootedTree


class TestSelectionAlgorithms(unittest.TestCase):
    """Test selection algorithms."""
    
    def test_median_of_medians(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        self.assertEqual(median_of_medians(arr, 1), 1)
        self.assertEqual(median_of_medians(arr, 4), 3)
        self.assertEqual(median_of_medians(arr, 8), 9)
    
    def test_quickselect(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        # Verify results match sorted array
        sorted_arr = sorted(arr)
        for k in range(1, len(arr) + 1):
            result = randomized_quickselect(arr, k)
            self.assertEqual(result, sorted_arr[k-1])


class TestDataStructures(unittest.TestCase):
    """Test data structures."""
    
    def test_dynamic_array(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr.size(), 2)
        
        arr.insert(1, 5)
        self.assertEqual(arr[1], 5)
        
        deleted = arr.delete(1)
        self.assertEqual(deleted, 5)
        self.assertEqual(arr.size(), 2)
    
    def test_matrix(self):
        mat = Matrix(2, 2)
        mat[0, 0] = 1
        mat[0, 1] = 2
        self.assertEqual(mat[0, 0], 1)
        
        transposed = mat.transpose()
        self.assertEqual(transposed[1, 0], 2)
    
    def test_stack(self):
        stack = ArrayStack()
        stack.push(1)
        stack.push(2)
        
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 1)
    
    def test_queue(self):
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        
        self.assertEqual(queue.front(), 1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size(), 1)
    
    def test_linked_list(self):
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(2)
        
        self.assertEqual(ll.search(2), 1)
        self.assertEqual(ll.size(), 2)
        
        ll.reverse()
        self.assertEqual(ll.to_list(), [2, 1])
    
    def test_tree(self):
        tree = RootedTree("A")
        tree.add_child("A", "B")
        tree.add_child("A", "C")
        
        self.assertEqual(tree.size(), 3)
        self.assertEqual(tree.preorder_traversal(), ["A", "B", "C"])


if __name__ == "__main__":
    unittest.main()
