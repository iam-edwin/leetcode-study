from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.findMinRecursive(nums, 0, len(nums) - 1)

    def findMinRecursive(self, nums: List[int], startIndex: int, endIndex: int) -> int:
        if nums[startIndex] < nums[endIndex]:
            return nums[startIndex]

        if startIndex == endIndex:
            return nums[startIndex]

        if startIndex + 1 == endIndex:
            return min(nums[startIndex], nums[endIndex])

        midIndex = (startIndex + endIndex) // 2

        if nums[startIndex] < nums[midIndex]:
            return self.findMinRecursive(nums, midIndex + 1, endIndex)
        else:
            return self.findMinRecursive(nums, startIndex, midIndex)
