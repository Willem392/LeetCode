class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        nums.append(0)
        for i in range(len(nums)-1):
            left += nums[i-1]
            right -= nums[i]
            if left == right:
                return i
        return -1