from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0

        for value in range(amount + 1):
            candidates = []
            for coin in coins:
                if value >= coin and dp[value - coin] != -1:
                    candidates.append(dp[value - coin] + 1)

            if len(candidates) > 0:
                dp[value] = min(candidates)

        return dp[amount]
