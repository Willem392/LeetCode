class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for ch in s:
                letters[ord(ch)-97] += 1
            res[tuple(letters)].append(s)
        return res.values()