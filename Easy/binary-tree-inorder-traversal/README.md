# [Easy] Binary Tree Inorder Traversal

## Complexity
Time Complexity: O(N), where N is the number of nodes in the binary tree, because each node is visited at most twice (once when pushed, once when popped).
Space Complexity: O(H), where H is the height of the tree, representing the maximum size of the stack. In the worst case of a skewed tree, this is O(N), and in the best case of a balanced tree, it is O(log N).

## Explanation
This solution implements an iterative inorder traversal (Left -> Root -> Right) using an explicit stack to mimic the call stack of a recursive solution. We initialize a pointer 'curr' at the root of the tree. In the outer loop, we traverse down to the leftmost node of the current subtree, pushing each visited node onto the stack. Once we hit a null child, we pop the top node from the stack, record its value, and then move to its right child to repeat the process. This continues until all nodes have been visited and the stack is empty.

## Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        stack = []
        curr = root
        
        while curr is not None or stack:
            # Reach the left most Node of the current Node
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            
            # Backtrack from the empty subtree and visit the node
            curr = stack.pop()
            result.append(curr.val)
            
            # We have visited the node and its left subtree. Now, it's the right subtree's turn
            curr = curr.right
            
        return result
```
