class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Turn these into sets so average is O(n) and worst is O(n^2)
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans1 = set()
        ans2 = set()
        for i in nums1:
            if i not in nums2 and i not in ans1:
                ans1.add(i)
        for i in nums2:
            if i not in nums1 and i not in ans2:
                ans2.add(i)
        return [ans1, ans2]