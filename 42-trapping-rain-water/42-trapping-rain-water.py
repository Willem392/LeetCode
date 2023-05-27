class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = height[0], height[len(height)-1]
        leftPointer, rightPointer = 0, len(height)-1
        total = 0
        while leftPointer != rightPointer:
            if maxL > maxR:
                rightPointer -= 1
                total += maxR - height[rightPointer] if maxR - height[rightPointer] > 0 else 0
                maxR = max(maxR, height[rightPointer])
            else:
                leftPointer += 1
                total += maxL - height[leftPointer] if maxL - height[leftPointer] > 0 else 0
                maxL = max(maxL, height[leftPointer])
        return total
                
            