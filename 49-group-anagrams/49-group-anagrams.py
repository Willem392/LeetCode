def count(s):
    letters = [0] * 26
    for ch in s:
        letters[ord(ch)-97] += 1
    return letters

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[tuple(count(s))].append(s)
        return res.values()