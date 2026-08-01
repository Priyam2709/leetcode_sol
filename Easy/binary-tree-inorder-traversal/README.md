# [Easy] Binary Tree Inorder Traversal

## Complexity
Time Complexity: O(N), where N is the number of nodes in the binary tree. Each node is pushed onto and popped from the stack exactly once.
Space Complexity: O(H), where H is the height of the tree, used by the stack. In the worst case of a skewed tree, the height is O(N). For a balanced tree, the space complexity is O(log N).

## Explanation
This solution performs an iterative inorder traversal (Left-Root-Right) of a binary tree using an auxiliary stack, satisfying the follow-up requirement to avoid recursion. We maintain a pointer 'curr' initialized to the root node. We push all left descendants of 'curr' onto the stack until 'curr' becomes null. Then, we pop the top element from the stack, visit it by appending its value to the result list, and transition 'curr' to its right child. This sequence of operations guarantees that nodes are processed in the correct order.

## Solution
```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result
```
