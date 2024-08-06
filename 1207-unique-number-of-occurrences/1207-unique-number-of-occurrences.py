class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        return len(set(d.values())) == len(d.values())