class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        l, res = [], []
        for elem in freq:
            l.append([freq[elem], elem])
        l = sorted(l)[::-1]
        for i in range(k):
            res.append(l[i][1])
        return res
            