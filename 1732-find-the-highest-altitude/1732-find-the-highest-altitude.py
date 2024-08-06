class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxa = 0
        cura = 0
        for i in range(len(gain)):
            cura += gain[i]
            maxa = max(cura, maxa)
        return maxa