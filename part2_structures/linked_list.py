"""
Linked List implementation
"""
from typing import Any, Optional


class ListNode:
    """Node for linked list."""
    def __init__(self, data: Any, next_node: Optional['ListNode'] = None):
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    """Singly linked list."""
    
    def __init__(self):
        self._head: Optional[ListNode] = None
        self._size = 0
    
    def prepend(self, data: Any) -> None:
        """Add to beginning. O(1)."""
        new_node = ListNode(data, self._head)
        self._head = new_node
        self._size += 1
    
    def append(self, data: Any) -> None:
        """Add to end. O(n)."""
        new_node = ListNode(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1
    
    def delete_first(self) -> Any:
        """Delete first element. O(1)."""
        if self._head is None:
            raise IndexError("List is empty")
        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        return data
    
    def search(self, data: Any) -> int:
        """Search for data. O(n). Returns index or -1."""
        current = self._head
        index = 0
        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
    
    def reverse(self) -> None:
        """Reverse list in-place. O(n)."""
        prev = None
        current = self._head
        while current is not None:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        self._head = prev
    
    def size(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._head is None
    
    def to_list(self) -> list:
        """Convert to Python list."""
        result = []
        current = self._head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result


if __name__ == "__main__":
    # Test linked list
    ll = SinglyLinkedList()
    for i in [1, 2, 3]:
        ll.append(i)
    print(f"List: {ll.to_list()}")
    
    ll.reverse()
    print(f"Reversed: {ll.to_list()}")
    
    print(f"Search 2: {ll.search(2)}")
    print(f"Delete first: {ll.delete_first()}")
    print(f"Final: {ll.to_list()}")
