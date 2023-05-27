class Solution:
    def trap(self, height: List[int]) -> int:
        leftTallest, rightTallest = [height[0]]*len(height), [height[len(height)-1]]*len(height)
        for i in range(1, len(height)):
            leftTallest[i] = max(leftTallest[i-1], height[i])
            rightTallest[len(height)-i-1] = max(height[len(height)-i-1], rightTallest[len(height)-i])
        total = 0
        for i in range(1, len(height)-1):
            total += min(leftTallest[i-1], rightTallest[i+1]) - height[i] if min(leftTallest[i-1], rightTallest[i+1]) - height[i] > 0 else 0
        return total
            