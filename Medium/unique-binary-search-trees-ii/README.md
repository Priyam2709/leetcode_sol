# [Medium] Unique Binary Search Trees II

## Complexity
Time Complexity: O(n * C_n), where C_n is the n-th Catalan number, representing the total number of unique BST structures. For each tree, we spend O(n) time to construct it. For n = 8, C_8 = 1430, which is extremely fast.
Space Complexity: O(n * C_n) to store all the generated unique binary search trees, plus O(n) auxiliary space for the recursion stack.

## Explanation
This problem is solved using a recursive divide-and-conquer approach with memoization. To generate all unique BSTs from 1 to n, we can pick each number 'i' in the range [start, end] to act as the root node. The left subtree of 'i' must be constructed from values in [start, i - 1], and the right subtree must be constructed from values in [i + 1, end]. We recursively generate all possible left and right subtrees, and then link them to the root node 'i'. Memoization is used to cache results for sub-ranges `(start, end)` to prevent redundant calculations and speed up execution.

## Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        memo = {}
        
        def generate(start, end):
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            
            memo[(start, end)] = all_trees
            return all_trees
        
        return generate(1, n)
```
