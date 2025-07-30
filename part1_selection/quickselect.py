"""
Randomized Quickselect - Expected O(n) selection algorithm
"""
from typing import List
import random


def randomized_quickselect(arr: List[int], k: int) -> int:
    """Find k-th smallest element in O(n) expected time."""
    if not arr or k < 1 or k > len(arr):
        raise ValueError("Invalid input")
    
    return _quickselect(arr.copy(), 0, len(arr) - 1, k - 1)


def _quickselect(arr: List[int], left: int, right: int, k: int) -> int:
    """Internal recursive quickselect function."""
    if left == right:
        return arr[left]
    
    # Random pivot
    pivot_idx = _partition(arr, left, right)
    
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return _quickselect(arr, left, pivot_idx - 1, k)
    else:
        return _quickselect(arr, pivot_idx + 1, right, k)


def _partition(arr: List[int], left: int, right: int) -> int:
    """Partition with random pivot."""
    # Choose random pivot
    rand_idx = random.randint(left, right)
    arr[rand_idx], arr[right] = arr[right], arr[rand_idx]
    
    pivot = arr[right]
    i = left
    
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[right] = arr[right], arr[i]
    return i


if __name__ == "__main__":
    # Test cases
    random.seed(42)
    test_arr = [3, 1, 4, 1, 5, 9, 2, 6]
    for k in [1, 3, 5, 8]:
        result = randomized_quickselect(test_arr, k)
        print(f"{k}-th smallest: {result}")
