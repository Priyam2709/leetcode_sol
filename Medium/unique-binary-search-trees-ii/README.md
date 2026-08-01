# [Medium] Unique Binary Search Trees II

## Complexity
Time Complexity: O(4^n / n^(1.5)), which is proportional to the Catalan number C_n representing the total number of unique BST structures. For each state, we iterate through all possible roots and combine the left and right subtrees.
Space Complexity: O(4^n / n^(1.5)) to store the generated trees in memory, and O(n) for the recursion call stack.

## Explanation
The problem can be solved recursively using a divide-and-conquer approach. For a range of values [start, end], we can pick any value 'i' in this range to be the root of the BST. The left subtree of 'i' must be constructed from the range [start, i - 1] and the right subtree must be constructed from [i + 1, end]. We recursively generate all possible left and right subtrees and combine them for each chosen root 'i'. To avoid redundant calculations and improve efficiency, we use memoization (caching results for already computed (start, end) ranges).

## Solution
```python
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
