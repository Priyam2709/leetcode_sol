# [Easy] Fizz Buzz

## Complexity
Time Complexity: O(n) because we iterate from 1 to n exactly once and perform constant-time arithmetic and string operations inside the loop.
Space Complexity: O(1) auxiliary space (excluding the output list which takes O(n) space).

## Explanation
We iterate through the numbers from 1 to n. For each number, we use conditional statements to check divisibility. We check divisibility by 15 first (since any number divisible by 15 is divisible by both 3 and 5) to append 'FizzBuzz'. Next, we check divisibility by 3 for 'Fizz' and by 5 for 'Buzz'. If none of these conditions are met, we convert the number to a string and append it to our result list.

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
