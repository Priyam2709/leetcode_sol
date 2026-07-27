# [Easy] Fizz Buzz

## Complexity
Time Complexity: O(n) because we iterate from 1 to n exactly once, performing constant time O(1) operations in each iteration. Space Complexity: O(1) auxiliary space (ignoring the space required for the output list of size n).

## Explanation
The solution iterates through numbers from 1 to n. For each number, it checks divisibility. If a number is divisible by both 3 and 5 (which is equivalent to being divisible by 15), we append 'FizzBuzz'. If it is only divisible by 3, we append 'Fizz'. If it is only divisible by 5, we append 'Buzz'. Otherwise, we convert the integer to a string and append it to the result list.

## Solution
```python
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
```
