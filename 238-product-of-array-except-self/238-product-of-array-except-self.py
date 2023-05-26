class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [nums[0]] * len(nums), [nums[len(nums)-1]] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = nums[i] * postfix[i+1]
        res = [0] * len(nums)
        res[0] = postfix[1]
        res[len(nums)-1] = prefix[len(nums)-2]
        for i in range(1, len(nums)-1):
            res[i] = prefix[i-1] * postfix[i+1]
        return res