"""
Median of Medians - Deterministic O(n) selection algorithm
"""
from typing import List


def median_of_medians(arr: List[int], k: int) -> int:
    """Find k-th smallest element in O(n) worst-case time."""
    if not arr or k < 1 or k > len(arr):
        raise ValueError("Invalid input")
    
    return _select(arr.copy(), k - 1)


def _select(arr: List[int], k: int) -> int:
    """Internal recursive selection function."""
    n = len(arr)
    
    # Base case: small arrays
    if n <= 5:
        arr.sort()
        return arr[k]
    
    # Find medians of groups of 5
    medians = []
    for i in range(0, n, 5):
        group = arr[i:i + 5]
        group.sort()
        medians.append(group[len(group) // 2])
    
    # Recursively find median of medians
    pivot = _select(medians, len(medians) // 2)
    
    # Partition around pivot
    pivot_idx = _partition(arr, pivot)
    
    # Recurse on appropriate side
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return _select(arr[:pivot_idx], k)
    else:
        return _select(arr[pivot_idx + 1:], k - pivot_idx - 1)


def _partition(arr: List[int], pivot: int) -> int:
    """Partition array around pivot value."""
    # Move pivot to end
    for i, val in enumerate(arr):
        if val == pivot:
            arr[i], arr[-1] = arr[-1], arr[i]
            break
    
    # Standard partition
    i = 0
    for j in range(len(arr) - 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[-1] = arr[-1], arr[i]
    return i


if __name__ == "__main__":
    # Test cases
    test_arr = [3, 1, 4, 1, 5, 9, 2, 6]
    for k in [1, 3, 5, 8]:
        result = median_of_medians(test_arr, k)
        print(f"{k}-th smallest: {result}")
