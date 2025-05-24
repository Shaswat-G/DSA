# We will be implementing creating a tree using level order traversal ungin double links and queueu ds
from collections import deque
from typing import Optional, Any, List
from dataclasses import dataclass


@dataclass
class Node:
    value: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: Any) -> None:
        new_node = Node(value)

        # edge case - empty tree
        if not self.root:
            self.root = new_node
            return

        # create a queue for level order traversal
        q = deque([self.root])
        while q:
            current_node = q.popleft()
            if not current_node.left:
                current_node.left = new_node
                return
            elif not current_node.right:
                current_node.right = new_node
                return
            q.extend([current_node.left, current_node.right])

    def __str__(self) -> str:
        if not self.root:
            return "<empty tree>"

        # Perform level-order traversal to collect nodes at each level
        result = []
        q = deque([(self.root, 0)])  # Queue stores (node, level)
        current_level = 0
        level_nodes = []

        while q:
            node, level = q.popleft()

            if level != current_level:
                result.append(" ".join(level_nodes))
                level_nodes = []
                current_level = level

            level_nodes.append(str(node.value))

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        # Append the last level
        if level_nodes:
            result.append(" ".join(level_nodes))

        return "\n".join(result)

    def preorder(self, node: Node):
        if node:
            print(node.value)
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)
        return

    def inorder(self, node: Node) -> None:
        if node:
            if node.left:
                self.inorder(node.left)
            print(node.value)
            if node.right:
                self.inorder(node.right)
        return 

    def postorder(self, node: Node) -> None:
        if node:
            if node.left:
                self.postorder(node.left)
            if node.right:
                self.postorder(node.right)
            print(node.value)
        return

    def levelorder(self) -> None:
        if not self.root:
            return None

        q = deque([self.root])

        while q:
            node = q.popleft()
            print(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def count_nodes(self, node : Node) -> int:
        if node:
            count_left = self.count_nodes(node.left)
            count_right = self.count_nodes(node.right)
            return 1 + count_left + count_right
        else:
            return 0

    def count_second_order_nodes(self, node:Node) -> int:
        if node:
            count_left = self.count_second_order_nodes(node.left)
            count_right = self.count_second_order_nodes(node.right)
            if node.left and node.right:
                return 1 + count_right + count_left
            else:
                return count_right + count_left
        else:
            return 0

    def count_first_order_nodes(self, node:Node) -> int:
        if node:
            count_left = self.count_first_order_nodes(node.left)
            count_right = self.count_first_order_nodes(node.right)
            if (node.left and not node.right) or (node.right and not node.left):
                return 1 + count_left + count_right
            else:
                return count_right + count_left
        else:
            return 0

# Removed redundant definition of count_first_order_nodes

    def count_leaf_nodes(self, node:Node) -> int:
        if node:
            if (not node.left) and (not node.right):
                return 1
            else:
                return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)
        else:
            return 0
    
    def sum_all_nodes(self, node:Node) -> int:
        if node:
            return node.value + self.sum_all_nodes(node.left) + self.sum_all_nodes(node.right)  
        else:
            return 0


def main():
    print("Hello Word!")

    bt = BinaryTree()

    for value in range(7):
        bt.insert(value)
        
    bt.levelorder()
    print(bt.count_nodes(bt.root))


if __name__ == "__main__":
    main()
