from typing import List, Set


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict: Set[str] = set()
        for word in wordDict:
            dict.add(word)

        dp = [False for _ in range(len(s))]

        dp[0] = s[0] in dict

        for i in range(1, len(s)):
            if s[: i + 1] in dict:
                dp[i] = True
            else:
                for j in range(i):
                    if dp[i - j - 1] == True and s[i - j : i + 1] in dict:
                        dp[i] = True
                        continue

        return dp[len(s) - 1]
