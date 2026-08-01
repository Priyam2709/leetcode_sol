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