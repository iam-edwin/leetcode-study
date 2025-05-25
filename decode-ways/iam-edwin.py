class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1

        for i in range(len(s)):
            if s[len(s) - 1 - i] == "0":
                dp[i + 1] = 0
            elif i == 0:
                dp[i + 1] = 1
            else:
                twoDigit = int(s[len(s) - 1 - i] + s[len(s) - i])
                if 1 <= twoDigit and twoDigit <= 26:
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]

        return dp[len(s)]
