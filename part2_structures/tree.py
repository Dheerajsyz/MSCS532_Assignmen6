"""
Rooted Tree implementation using linked structure
"""
from typing import Any, List, Optional


class TreeNode:
    """Node for rooted tree."""
    def __init__(self, data: Any):
        self.data = data
        self.children: List['TreeNode'] = []
        self.parent: Optional['TreeNode'] = None
    
    def add_child(self, child: 'TreeNode') -> None:
        """Add child. O(1)."""
        child.parent = self
        self.children.append(child)
    
    def is_leaf(self) -> bool:
        return len(self.children) == 0


class RootedTree:
    """Rooted tree with linked representation."""
    
    def __init__(self, root_data: Any = None):
        self.root = TreeNode(root_data) if root_data is not None else None
        self._size = 1 if root_data is not None else 0
    
    def add_child(self, parent_data: Any, child_data: Any) -> bool:
        """Add child to parent. O(n) to find parent."""
        parent_node = self._find_node(parent_data)
        if parent_node is None:
            return False
        
        child_node = TreeNode(child_data)
        parent_node.add_child(child_node)
        self._size += 1
        return True
    
    def _find_node(self, data: Any) -> Optional[TreeNode]:
        """Find node with data. O(n)."""
        if self.root is None:
            return None
        return self._find_recursive(self.root, data)
    
    def _find_recursive(self, node: TreeNode, data: Any) -> Optional[TreeNode]:
        if node.data == data:
            return node
        for child in node.children:
            result = self._find_recursive(child, data)
            if result is not None:
                return result
        return None
    
    def preorder_traversal(self) -> List[Any]:
        """Preorder traversal. O(n)."""
        if self.root is None:
            return []
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node: TreeNode, result: List[Any]) -> None:
        result.append(node.data)
        for child in node.children:
            self._preorder_recursive(child, result)
    
    def level_order_traversal(self) -> List[Any]:
        """Level-order traversal. O(n)."""
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            queue.extend(node.children)
        
        return result
    
    def size(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self.root is None


if __name__ == "__main__":
    # Test tree
    tree = RootedTree("A")
    tree.add_child("A", "B")
    tree.add_child("A", "C")
    tree.add_child("B", "D")
    
    print(f"Tree size: {tree.size()}")
    print(f"Preorder: {tree.preorder_traversal()}")
    print(f"Level-order: {tree.level_order_traversal()}")
