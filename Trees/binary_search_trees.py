from collections import deque


class Node:
    def __init__(self, data: int, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value: int) -> None:

        new_node = Node(value)

        # Emmpty Tree
        if not self.root:
            self.root = new_node

        # Finite Tree
        else:
            # Find the next place to insert -> level order traversal
            q = deque([self.root])

            while q:
                node = q.popleft()
                if not node.left:
                    node.left = new_node
                    break
                elif not node.right:
                    node.right = new_node
                    break
                else:
                    q.append(node.left)
                    q.append(node.right)

        self.size += 1
        return

    def preorder(self, node: Node) -> None:
        # root, left subtree, right subtree
        if node:
            print(node.data)
            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)
        return

    def inorder(self, node: Node) -> None:

        if node:
            if node.left:
                self.inorder(node.left)
            print(node.data)
            if node.right:
                self.inorder(node.right)

        return

    def postorder(self, node: Node) -> None:

        if node:
            if node.left:
                self.postorder(node.left)
            if node.right:
                self.postorder(node.right)
            print(node.data)

        return

    def levelorder(self) -> None:

        if not self.root:
            return

        q = deque([self.root])

        while q:
            node = q.popleft()
            print(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return

    def __len__(self):
        return self.size

    def __str__(self):
        # level order traversal.
        if not self.root:
            return "<Empty Tree>"

        result = []
        level = 0
        level_nodes = []
        q = deque([(self.root, 0)])
        while q:
            node, node_level = q.popleft()

            # level changed
            if level != node_level:
                level_nodes_string = " ".join(level_nodes)
                result.append(f"Level {level} : {level_nodes_string}")
                level = node_level
                level_nodes = []
            # unchanged

            level_nodes.append(str(node.data))

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        level_nodes_string = " ".join(level_nodes)
        result.append(f"Level {level} : {level_nodes_string}")

        return "\n".join(result)

    def search_bst(self, query : int) -> bool:
        if not self.root:
            return False

        current = self.root
        while current:
            if current.data == query:
                return True
            if current.data > query:
                current = current.left
            else:
                current = current.right
        return False

    def insert_bst(self, value : int) -> None:

        new_node = Node(value)

        if not self.root:
            self.root = new_node

        else:
            # search to find its place, if found do not put, if not found insert there
            prev_node = None
            current = self.root
            while current:
                if current.data == value:
                    return
                if value < current.data:
                    prev_node = current
                    current = current.left
                else:
                    prev_node = current
                    current = current.right

            if value < prev_node.data:
                prev_node.left = new_node
            else:
                prev_node.right = new_node

        self.size +=1
        return

    def delete_bst(self, value: int) -> None:
        def delete(sub_root : Node, value : int):
            if not sub_root:
                return None
            elif value > sub_root.data:
                sub_root.right = delete(sub_root.right, value)
            elif value < sub_root.data:
                sub_root.left = delete(sub_root.left, value)
                
            else: # sub_root.data is eq to value
                if (not sub_root.left) and (not sub_root.right):
                    return None
                elif not sub_root.left:
                    return sub_root.right
                elif not sub_root.right:
                    return sub_root.left
                else:
                    # both children exist
                    # find the next pre-order element to replace it with.
                    current = sub_root.right
                    while current.left:
                        current = current.left
                    # current will have the next pre-order element. => swap and delete
                    sub_root.data = current.data
                    sub_root.right = delete(sub_root.right, current.data)
        
        self.root = delete(self.root, value)
        return None

def main():
    b_tree = BinaryTree()
    for value in range(10):
        b_tree.insert_bst(value)
    print(f"Length of Binary Tree : {len(b_tree)}")
    print(b_tree)
    b_tree.preorder(b_tree.root)
    b_tree.inorder(b_tree.root)


if __name__ == "__main__":
    main()
