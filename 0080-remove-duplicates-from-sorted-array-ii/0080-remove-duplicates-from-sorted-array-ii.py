class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        curCount = 0
        curVal = float('inf')
        for index in range(len(nums)):
            i = nums[index-k]
            if i != curVal:
                curCount = 1
                curVal = i
            elif curCount < 2:
                curCount += 1
            else:
                nums.append(nums.pop(index-k))
                k += 1
        return len(nums)-k