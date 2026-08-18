class Solution:
    def countAndSay(self, n: int) -> str:
        curr = "1"
        for _ in range(1, n):
            next_str = []
            i = 0
            n_len = len(curr)
            while i < n_len:
                count = 1
                while i + 1 < n_len and curr[i] == curr[i+1]:
                    i += 1
                    count += 1
                next_str.append(str(count))
                next_str.append(curr[i])
                i += 1
            curr = "".join(next_str)
        return curr