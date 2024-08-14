class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        max_avg = float('-inf')
        for i in range(k):
            total += nums[i]
        l, r = 0, k
        max_avg = total / k
        while r < len(nums):
            total += nums[r]
            r += 1
            total -= nums[l]
            l += 1
            max_avg = max(max_avg, total / k)
        return max_avg