"""
Assignment 6 Demo - Selection Algorithms & Data Structures
MSCS532 - Dheeraj K
"""
import time
import random
from part1_selection.median_of_medians import median_of_medians
from part1_selection.quickselect import randomized_quickselect
from part2_structures.arrays import DynamicArray, Matrix
from part2_structures.stack_queue import ArrayStack, ArrayQueue
from part2_structures.linked_list import SinglyLinkedList
from part2_structures.tree import RootedTree


def demo_part1():
    """Demo Part 1: Selection Algorithms"""
    print("=== PART 1: SELECTION ALGORITHMS ===")
    
    # Test arrays
    arrays = {
        "Random": [3, 1, 4, 1, 5, 9, 2, 6, 5],
        "Sorted": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "Reverse": [9, 8, 7, 6, 5, 4, 3, 2, 1]
    }
    
    for name, arr in arrays.items():
        print(f"\n{name} array: {arr}")
        k = len(arr) // 2  # Find median
        
        # Compare algorithms
        mom_result = median_of_medians(arr, k)
        qs_result = randomized_quickselect(arr, k)
        sorted_result = sorted(arr)[k-1]
        
        print(f"  {k}-th smallest element:")
        print(f"    Median of Medians: {mom_result}")
        print(f"    Randomized Quickselect: {qs_result}")
        print(f"    Sorting-based: {sorted_result}")
        print(f"    All correct: {mom_result == qs_result == sorted_result}")


def demo_part2():
    """Demo Part 2: Data Structures"""
    print("\n=== PART 2: DATA STRUCTURES ===")
    
    # Dynamic Array
    print("\n--- Dynamic Array ---")
    arr = DynamicArray()
    for i in range(5):
        arr.append(i)
    print(f"After appending 0-4: {arr}")
    arr.insert(2, 99)
    print(f"After inserting 99 at index 2: {arr}")
    
    # Matrix
    print("\n--- Matrix ---")
    mat = Matrix(2, 2)
    mat[0, 0], mat[0, 1] = 1, 2
    mat[1, 0], mat[1, 1] = 3, 4
    print(f"Matrix [0,1]: {mat[0, 1]}")
    
    # Stack
    print("\n--- Stack ---")
    stack = ArrayStack()
    for i in range(3):
        stack.push(i)
    print(f"Stack size: {stack.size()}")
    print(f"Popped: {stack.pop()}")
    
    # Queue
    print("\n--- Queue ---")
    queue = ArrayQueue()
    for i in range(3):
        queue.enqueue(i)
    print(f"Queue size: {queue.size()}")
    print(f"Dequeued: {queue.dequeue()}")
    
    # Linked List
    print("\n--- Linked List ---")
    ll = SinglyLinkedList()
    for i in [1, 2, 3]:
        ll.append(i)
    print(f"List: {ll.to_list()}")
    ll.reverse()
    print(f"Reversed: {ll.to_list()}")
    
    # Tree
    print("\n--- Tree ---")
    tree = RootedTree("A")
    tree.add_child("A", "B")
    tree.add_child("A", "C")
    tree.add_child("B", "D")
    print(f"Preorder: {tree.preorder_traversal()}")
    print(f"Level-order: {tree.level_order_traversal()}")


def performance_analysis():
    """Basic performance analysis"""
    print("\n=== PERFORMANCE ANALYSIS ===")
    
    sizes = [100, 1000, 5000]
    print("\nTiming selection algorithms:")
    
    for size in sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        k = size // 2
        
        # Time Median of Medians
        start = time.time()
        mom_result = median_of_medians(arr, k)
        mom_time = time.time() - start
        
        # Time Quickselect
        start = time.time()
        qs_result = randomized_quickselect(arr, k)
        qs_time = time.time() - start
        
        # Time sorting approach
        start = time.time()
        sort_result = sorted(arr)[k-1]
        sort_time = time.time() - start
        
        print(f"\nSize {size}:")
        print(f"  Median of Medians: {mom_time:.6f}s")
        print(f"  Randomized Quickselect: {qs_time:.6f}s")
        print(f"  Sorting: {sort_time:.6f}s")
        print(f"  Results match: {mom_result == qs_result == sort_result}")


def complexity_summary():
    """Print complexity analysis"""
    print("\n=== COMPLEXITY SUMMARY ===")
    
    complexities = {
        "Selection Algorithms": {
            "Median of Medians": "O(n) worst-case",
            "Randomized Quickselect": "O(n) expected, O(n²) worst",
            "Sorting-based": "O(n log n)"
        },
        "Data Structures": {
            "Array access": "O(1)",
            "Array insert/delete": "O(n)",
            "Stack push/pop": "O(1)",
            "Queue enqueue/dequeue": "O(1)",
            "Linked list prepend": "O(1)",
            "Linked list append": "O(n)",
            "Tree search": "O(n)"
        }
    }
    
    for category, items in complexities.items():
        print(f"\n{category}:")
        for operation, complexity in items.items():
            print(f"  {operation}: {complexity}")


def main():
    """Main execution"""
    print("Assignment 6: Medians, Order Statistics & Elementary Data Structures")
    print("MSCS532 - Dheeraj K")
    
    # Set seed for reproducible results
    random.seed(42)
    
    demo_part1()
    demo_part2()
    performance_analysis()
    complexity_summary()
    
    print("\n=== ASSIGNMENT COMPLETED ===")
    print("Run 'python -m pytest tests/' for unit tests")


if __name__ == "__main__":
    main()
