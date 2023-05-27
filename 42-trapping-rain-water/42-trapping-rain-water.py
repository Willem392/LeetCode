class Solution:
    def trap(self, height: List[int]) -> int:
        s = set()
        for i in range(len(height)):
            s.add((height[i], i))
        l = sorted([*s])[::-1]
        leftTallest = height[0]
        rightTallest = l[0][0]
        total = 0
        for i in range(1, len(height)-1):
            leftTallest = max(leftTallest, height[i - 1])
            while i >= l[0][1]:
                l.pop(0)
            rightTallest = l[0][0]
            total += min(leftTallest, rightTallest) - height[i] if min(leftTallest, rightTallest) - height[i] > 0 else 0
        return total
            