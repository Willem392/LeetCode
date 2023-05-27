class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftTallest, rightTallest = [height[0]]*n, [height[n-1]]*n
        for i in range(1, n):
            leftTallest[i] = max(leftTallest[i-1], height[i])
            rightTallest[n-i-1] = max(height[n-i-1], rightTallest[n-i])
        total = 0
        for i in range(1, n-1):
            total += min(leftTallest[i-1], rightTallest[i+1]) - height[i] if min(leftTallest[i-1], rightTallest[i+1]) - height[i] > 0 else 0
        return total
            