class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            tempNums = list(nums)
            tempNums.remove(i)
            while i in tempNums:
                tempNums.remove(i)
                nums.remove(i)