class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = []
        a.append(0)
        for i in range(len(gain)):
            a.append(a[i] + gain[i])
        return max(a)