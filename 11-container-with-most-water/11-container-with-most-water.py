class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height)-1
        while(left != right):
            distance = right - left
            area = min(height[left], height[right]) * distance
            maxArea = max(area, maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea