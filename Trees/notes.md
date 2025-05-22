Trees are collection of nodes and edges.

n nodes -> n-1 edges (1 edge for each node except the root)

The root node is the top node of the tree. It has no parent.
The leaf node is the bottom node of the tree. It has no children.
The internal node is any node that has children. It is not a leaf node.

The depth of a node is the number of edges from the root to that node.
The height of a node is the number of edges from that node to the deepest leaf node.
The height of a tree is the height of the root node.
The level of a node is the number of edges from the root to that node.
The level of a tree is the number of edges from the root to the deepest leaf node.
The degree of a node is the number of children it has.
The degree of a tree is the maximum degree of any node in the tree.
The subtree of a node is the tree formed by that node and all its descendants. (disjoint)
The ancestor of a node is any node on the path from the root to that node.
The descendant of a node is any node on the path from that node to the leaf nodes.
The sibling of a node is any node that has the same parent as that node.
The path of a node is the sequence of nodes from the root to that node.
The forest of a tree is the collection of all its subtrees.
The binary tree is a tree in which each node has at most two children.
The binary search tree is a binary tree in which the left child of a node is less than the node and the right child is greater than the node.
The complete binary tree is a binary tree in which all levels are completely filled except possibly the last level, which is filled from left to right.


children -> immediate descendants
Sublings -> children of the same parent
Descnedants -> all children, grandchildren, etc.
Ancestors -> all parents, grandparents, etc.
Leaf nodes -> terminal nodes -> no children -> 0 degree

root is level 1
next is level 2
and so on

binary tree
- each node has at most 2 children - children can be 0, 1, or 2
- left child and right child, left skewed vs right skewed

Number of Binary Trees with n nodes
- in unlabeled binary trees, the number of binary trees with n nodes is given by the Catalan number C(n) = (2n)! / (n! * (n + 1)!) = 2nCn / (n + 1)

Number of trees with maximum height h
- in unlabeled binary trees, the number of binary trees with maximum height h is given by 2 power h - 1
- recursive formula: T(n, h) = T(n - 1, h - 1) + T(n - 2, h - 1) + ... + T(0, h - 1)
- in labeled binary tree just multiply by n! to catalan number


foe hiehght h
min nodes = h+1
max nodes = 2 power (h+1) - 1 

hi
