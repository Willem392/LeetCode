class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            if s.get(target-nums[i]) != None:
                return [s.get(target-nums[i]), i]
            s.update({nums[i]: i})