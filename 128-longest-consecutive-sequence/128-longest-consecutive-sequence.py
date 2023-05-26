class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestCount = 0
        s = set(nums)
        for n in nums:
            count = 0
            if n - 1 not in s:
                while n in s:
                    count += 1
                    n += 1
                longestCount = max(count, longestCount)
        return longestCount