"""
Dynamic Array implementation
"""
from typing import Any, List


class DynamicArray:
    """Array with automatic resizing."""
    
    def __init__(self):
        self._capacity = 10
        self._size = 0
        self._data = [None] * self._capacity
    
    def __getitem__(self, index: int) -> Any:
        if not 0 <= index < self._size:
            raise IndexError("Index out of range")
        return self._data[index]
    
    def __setitem__(self, index: int, value: Any) -> None:
        if not 0 <= index < self._size:
            raise IndexError("Index out of range")
        self._data[index] = value
    
    def append(self, value: Any) -> None:
        """Add element to end. O(1) amortized."""
        if self._size >= self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1
    
    def insert(self, index: int, value: Any) -> None:
        """Insert element at index. O(n)."""
        if not 0 <= index <= self._size:
            raise IndexError("Index out of range")
        if self._size >= self._capacity:
            self._resize(2 * self._capacity)
        
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1
    
    def delete(self, index: int) -> Any:
        """Delete element at index. O(n)."""
        if not 0 <= index < self._size:
            raise IndexError("Index out of range")
        
        value = self._data[index]
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        return value
    
    def size(self) -> int:
        return self._size
    
    def _resize(self, new_capacity: int) -> None:
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
    
    def __str__(self) -> str:
        return str([self._data[i] for i in range(self._size)])


class Matrix:
    """2D Matrix implementation."""
    
    def __init__(self, rows: int, cols: int, default=0):
        self.rows = rows
        self.cols = cols
        self._data = [[default] * cols for _ in range(rows)]
    
    def __getitem__(self, key) -> Any:
        row, col = key
        return self._data[row][col]
    
    def __setitem__(self, key, value: Any) -> None:
        row, col = key
        self._data[row][col] = value
    
    def transpose(self) -> 'Matrix':
        """Return transposed matrix. O(rows * cols)."""
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result[j, i] = self[i, j]
        return result


if __name__ == "__main__":
    # Test array
    arr = DynamicArray()
    for i in range(5):
        arr.append(i)
    print(f"Array: {arr}")
    
    # Test matrix
    mat = Matrix(2, 2)
    mat[0, 0] = 1
    mat[0, 1] = 2
    mat[1, 0] = 3
    mat[1, 1] = 4
    print(f"Matrix element [0,1]: {mat[0, 1]}")
