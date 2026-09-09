class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        start = 1000
        commas = 1

        while start <= n:
            end = min(n, start * 1000 - 1)

            # Number of integers in this range
            count = end - start + 1

            ans += count * commas

            start *= 1000
            commas += 1

        return ans


