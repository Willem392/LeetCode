class Solution:
    def trap(self, height: List[int]) -> int:
        leftPointer, rightPointer = 0, len(height)-1
        maxL, maxR = height[leftPointer], height[rightPointer]
        total = 0
        while leftPointer != rightPointer:
            if maxL > maxR:
                rightPointer -= 1
                maxR = max(maxR, height[rightPointer])
                total += maxR - height[rightPointer]
            else:
                leftPointer += 1
                maxL = max(maxL, height[leftPointer])
                total += maxL - height[leftPointer]
        return total
                
            