# Binary Trees & Binary Search Trees (BSTs): Comprehensive Notes

## 1. What is a Tree?

A **tree** is a hierarchical, non-linear data structure consisting of nodes and edges. It models relationships where each node (except the root) has exactly one parent, and nodes may have zero or more children. Trees are acyclic and connected.

- **n nodes ⇒ n-1 edges** (one edge for each node except the root)
- **Root node:** The unique top node with no parent.
- **Leaf node:** A node with no children (terminal node, degree 0).
- **Internal node:** Any node with at least one child (not a leaf).
- **Subtree:** A tree formed by a node and all its descendants.
- **Ancestor/Descendant:** Ancestor is any node on the path from root to a node; descendant is any node in the subtree rooted at a node.
- **Sibling:** Nodes sharing the same parent.
- **Path:** Sequence of nodes from root to a given node.
- **Forest:** A collection of disjoint trees (removing the root splits a tree into a forest).

## 2. Key Properties & Terminology

- **Depth of a node:** Number of edges from root to that node.
- **Height of a node:** Number of edges from that node to the deepest leaf.
- **Height of a tree:** Height of the root node.
- **Level of a node:** Often defined as depth + 1 (root is level 1).
- **Degree of a node:** Number of children.
- **Degree of a tree:** Maximum degree among all nodes.

## 3. Types of Binary Trees

- **Binary Tree:** Each node has at most two children (left and right).
- **Full Binary Tree:** Every node has 0 or 2 children.
- **Perfect Binary Tree:** All internal nodes have 2 children, all leaves at same level.
- **Complete Binary Tree:** All levels are fully filled except possibly the last, which is filled left to right.
- **Skewed Binary Tree:** All nodes have only left or only right child (degenerates to a list).
- **Balanced Binary Tree:** Height is O(log n); ensures efficient operations.

## 4. Binary Search Tree (BST)

A **BST** is a binary tree with the property:

- For any node, all values in the left subtree are less, all values in the right subtree are greater.
- No duplicate values (in classic BSTs).
- Enables efficient search, insert, and delete (O(log n) average for balanced BSTs).

## 5. Catalan Numbers & Counting Trees

- **Number of unlabeled binary trees with n nodes:** Catalan number C(n) = (2n)! / (n! \* (n+1)!)
- **Number of labeled binary trees:** n! \* C(n)
- **Minimum nodes for height h:** h+1
- **Maximum nodes for height h:** 2^(h+1) - 1

## 6. Traversal Orders

- **Preorder:** Root → Left → Right
- **Inorder:** Left → Root → Right (yields sorted order for BST)
- **Postorder:** Left → Right → Root
- **Level Order:** Breadth-first, level by level
- Pre-order, post-order and in-order alone cannot uniquely identify a binary tree (catalan number of possibilites).
- A combination of pre-order and post-order also cannot uniquely identify a binary tree, the exact number is not known.
- However, give an inorder, any of post or pre can uniquely identify a binary tree. Why? splitting of nodes in the left and right subtree is unique.

## 7. Common Operations

- **Search, Insert, Delete (BST):** O(h) time, h = height
- **Find min/max:** Leftmost/rightmost node
- **Successor/Predecessor:** Next/previous in sorted order
- **Balance Checking:** AVL, Red-Black, etc.
- **Serialization/Deserialization:** Convert tree to/from string/array

## 8. Applications

- **Hierarchical data modeling** (file systems, organization charts)
- **Expression parsing/evaluation**
- **Auto-complete, prefix trees (tries)**
- **Database indexing (B/B+ trees)**
- **Efficient searching, range queries (BSTs)**

## 9. Counting Nodes:
- Usually we do post order style traversal to count nodes with some conditional recursion - left, right and root.
- Inversion of binary tree is simple, just swap left and right children recursively.
- Maximum depth of a binary tree is the longest path from root to leaf = height of the tree = 1 + max(depth of left subtree, depth of right subtree).
- The height of every node in a binary tree can be calculated as max(left height, right height) + 1.
- The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
- The maximum length of path that passes through a given node is the sum of the left height and right height of the node. => max diameter = max(max_paths of all nodes)
- While counting edges, the base case is returning -1 so that when you define left heights and right heights, you can add 1 to the sum of left and right heights to get the number of edges (0 for lead nodes.)
---

## Recognizing and Applying Binary Trees & BSTs: Problem Patterns & Use Cases

### 1. Classic Problems Solvable with Binary Trees / BSTs

**1. Tree Traversals (Preorder, Inorder, Postorder, Level Order)**  
_Essential Idea:_ Visit all nodes in a specific order for searching, printing, or processing.  
_Binary Tree Use:_ Recursively or iteratively visit nodes; inorder traversal of BST yields sorted order.

**2. Search, Insert, Delete in BST**  
_Essential Idea:_ Maintain a dynamic set with fast search, insert, and delete.  
_BST Use:_ O(log n) average-case for balanced BSTs; structure ensures left < root < right.

**3. Find Min/Max, Successor/Predecessor**  
_Essential Idea:_ Quickly find smallest/largest or next/previous value.  
_BST Use:_ Min is leftmost, max is rightmost; successor/predecessor via traversal.

**4. Validate BST**  
_Essential Idea:_ Check if a tree satisfies BST property.  
_BST Use:_ Recursively check left < node < right for all nodes.

**5. Lowest Common Ancestor (LCA)**  
_Essential Idea:_ Find the deepest shared ancestor of two nodes.  
_Binary Tree Use:_ Traverse both subtrees; BST allows O(h) search using value comparisons.

**6. Height/Depth/Balance Checking**  
_Essential Idea:_ Compute height, check if tree is balanced (AVL, Red-Black, etc.).  
_Binary Tree Use:_ Recursively compute heights, check balance at each node.

**7. Diameter/Max Path Sum**  
_Essential Idea:_ Find the longest path or max sum path between any two nodes.  
_Binary Tree Use:_ Recursively compute for each node.

**8. Symmetry, Mirror, and Isomorphism**  
_Essential Idea:_ Check if two trees are mirror images or structurally identical.  
_Binary Tree Use:_ Recursively compare left/right subtrees.

**9. Serialize/Deserialize Tree**  
_Essential Idea:_ Convert tree to string/array and back.  
_Binary Tree Use:_ Use traversal order to encode/decode structure.

**10. Construct Tree from Traversals**  
_Essential Idea:_ Rebuild tree from preorder/inorder/postorder arrays.  
_Binary Tree Use:_ Recursively partition arrays to build subtrees.

**11. Convert Sorted Array/List to BST**  
_Essential Idea:_ Build height-balanced BST from sorted data.  
_BST Use:_ Recursively pick middle as root.

**12. Kth Smallest/Largest in BST**  
_Essential Idea:_ Find kth order statistic efficiently.  
_BST Use:_ Inorder traversal, or augment with subtree sizes.

**13. Range Queries (Sum, Count, etc.)**  
_Essential Idea:_ Query/count values in a range.  
_BST Use:_ Traverse only relevant subtrees.

**14. Tree to Linked List (Flattening)**  
_Essential Idea:_ Convert tree to a list in a specific order.  
_Binary Tree Use:_ Inorder/preorder traversal, relink nodes.

**15. Path Sum/Root-to-Leaf Paths**  
_Essential Idea:_ Find/count all paths with a given sum.  
_Binary Tree Use:_ Recursively track path sums.

**16. Balanced BSTs (AVL, Red-Black, Treap, etc.)**  
_Essential Idea:_ Maintain O(log n) operations by keeping tree balanced.  
_BST Use:_ Rotations and balance checks after insert/delete.

**17. BST Iterator/Successor Generator**  
_Essential Idea:_ Iterate BST in sorted order with O(h) space.  
_BST Use:_ Stack-based inorder traversal.

**18. Recover BST/Correct Swapped Nodes**  
_Essential Idea:_ Fix a BST where two nodes are swapped.  
_BST Use:_ Inorder traversal to detect and fix.

**19. Tree Views (Left, Right, Top, Bottom)**  
_Essential Idea:_ Print nodes visible from a side.  
_Binary Tree Use:_ Level order traversal with position tracking.

**20. Tree Reconstruction/Cloning**  
_Essential Idea:_ Deep copy or reconstruct a tree.  
_Binary Tree Use:_ Recursively copy nodes and structure.

### 2. Real-World & Interview/LeetCode Binary Tree/BST Problems

- **Binary Tree Inorder Traversal** (LeetCode 94): Traversal.
- **Validate Binary Search Tree** (LeetCode 98): BST property check.
- **Lowest Common Ancestor of BST** (LeetCode 235): BST property for O(h) search.
- **Lowest Common Ancestor of Binary Tree** (LeetCode 236): General tree LCA.
- **Convert Sorted Array to BST** (LeetCode 108): Build balanced BST.
- **Kth Smallest Element in BST** (LeetCode 230): Inorder traversal.
- **Serialize and Deserialize Binary Tree** (LeetCode 297): Encode/decode tree.
- **Binary Tree Maximum Path Sum** (LeetCode 124): Max path sum.
- **Symmetric Tree** (LeetCode 101): Mirror check.
- **Balanced Binary Tree** (LeetCode 110): Height/balance check.
- **Diameter of Binary Tree** (LeetCode 543): Longest path.
- **Flatten Binary Tree to Linked List** (LeetCode 114): In-place flattening.
- **Recover Binary Search Tree** (LeetCode 99): Fix swapped nodes.
- **Binary Search Tree Iterator** (LeetCode 173): Inorder iterator.
- **Range Sum of BST** (LeetCode 938): Range query.
- **Construct Binary Tree from Preorder and Inorder Traversal** (LeetCode 105): Tree construction.
- **Construct Binary Tree from Inorder and Postorder Traversal** (LeetCode 106): Tree construction.
- **Populating Next Right Pointers in Each Node** (LeetCode 116, 117): Level order traversal.
- **Path Sum** (LeetCode 112, 113): Root-to-leaf path sums.
- **Count Complete Tree Nodes** (LeetCode 222): Complete tree properties.
- **Convert BST to Greater Tree** (LeetCode 538): Reverse inorder traversal.
- **Find Mode in BST** (LeetCode 501): Inorder traversal with frequency count.
- **Minimum Absolute Difference in BST** (LeetCode 530): Inorder traversal.
- **Increasing Order Search Tree** (LeetCode 897): Inorder relinking.
- **All Nodes Distance K in Binary Tree** (LeetCode 863): Tree traversal.
- **Delete Node in a BST** (LeetCode 450): BST delete operation.
- **Trim a Binary Search Tree** (LeetCode 669): Prune nodes outside range.
- **Closest Binary Search Tree Value** (LeetCode 270): Closest value search.
- **BST to Doubly Linked List** (LeetCode 426): Inorder relinking.

_This list covers all classic and modern binary tree/BST problems. If a problem involves hierarchical data, recursive structure, sorted dynamic sets, or efficient range queries, think of binary trees and BSTs!_
