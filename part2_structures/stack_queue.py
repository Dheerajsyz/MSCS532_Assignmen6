"""
Stack and Queue implementations using arrays
"""
from typing import Any


class ArrayStack:
    """Stack using dynamic array. LIFO."""
    
    def __init__(self):
        self._data = []
    
    def push(self, item: Any) -> None:
        """Push item. O(1) amortized."""
        self._data.append(item)
    
    def pop(self) -> Any:
        """Pop item. O(1)."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()
    
    def peek(self) -> Any:
        """Peek at top. O(1)."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]
    
    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def size(self) -> int:
        return len(self._data)


class ArrayQueue:
    """Queue using circular array. FIFO."""
    
    def __init__(self):
        self._capacity = 10
        self._data = [None] * self._capacity
        self._size = 0
        self._front = 0
    
    def enqueue(self, item: Any) -> None:
        """Add to rear. O(1) amortized."""
        if self._size >= self._capacity:
            self._resize()
        
        rear = (self._front + self._size) % self._capacity
        self._data[rear] = item
        self._size += 1
    
    def dequeue(self) -> Any:
        """Remove from front. O(1)."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item
    
    def front(self) -> Any:
        """Peek at front. O(1)."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[self._front]
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def size(self) -> int:
        return self._size
    
    def _resize(self) -> None:
        new_capacity = 2 * self._capacity
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[(self._front + i) % self._capacity]
        self._data = new_data
        self._capacity = new_capacity
        self._front = 0


if __name__ == "__main__":
    # Test stack
    stack = ArrayStack()
    for i in range(3):
        stack.push(i)
    print(f"Stack size: {stack.size()}")
    print(f"Popped: {stack.pop()}")
    
    # Test queue
    queue = ArrayQueue()
    for i in range(3):
        queue.enqueue(i)
    print(f"Queue size: {queue.size()}")
    print(f"Dequeued: {queue.dequeue()}")
