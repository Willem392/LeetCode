class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1
        for i in nums2:
            merged.append(i)
        merged.sort()
        length = len(merged)
        if len(merged) % 2 == 0:
            median = merged[int(len(merged)/2)-1] + merged[int(len(merged)/2)]
            median /= 2
        else:
            median = merged[int(len(merged)/2)]
        return median
        