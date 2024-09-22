class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for c in range(m, n+m):
            nums1[c] = nums2[c-m]
        s = sorted(nums1)
        for c in range(m+n):
            nums1[c] = s[c]