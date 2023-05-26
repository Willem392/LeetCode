class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        """lists = [[]for i in range(len(nums) + 1)]
        for key, val in freq.items():
            lists[val].append(key)
        res = []
        for i in range(len(lists)-1, 0, -1):
            for n in lists[i]:
                res.append(n)
                if len(res) == k:
                    return res"""
        l, res = [], []
        for key, val in freq.items():
            l.append([val, key])
        l = sorted(l)[::-1]
        for i in range(k):
            res.append(l[i][1])
        return res
            