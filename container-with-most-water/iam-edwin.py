from typing import List


class Solution:
    def maxAreaSlow(self, height: List[int]) -> int:
        maxArea = 0

        for i in range(1, len(height)):
            subMaxArea = 0
            for j in range(i):
                h = min(height[i], height[j])
                subMaxArea = max(subMaxArea, (i - j) * h)

            maxArea = max(maxArea, subMaxArea)

        return maxArea

    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        n = len(height)
        left = 0
        right = n - 1

        while left < right:
            leftHeight = height[left]
            rightHeight = height[right]
            lowHeight = min(leftHeight, rightHeight)
            area = (right - left) * lowHeight
            maxArea = max(maxArea, area)

            if leftHeight > rightHeight:
                right -= 1
                while right >= 0 and height[right] <= rightHeight:
                    right -= 1
            else:
                left += 1
                while left < n and leftHeight >= height[left]:
                    left += 1

        return maxArea
