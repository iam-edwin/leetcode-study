from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = 0

        for i in range(len(nums)):
            if sum <= 0:
                sum = nums[i]
            else:
                sum += nums[i]
            maxSum = max(maxSum, sum)

        return maxSum
