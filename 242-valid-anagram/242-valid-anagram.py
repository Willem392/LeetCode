class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        sSet, tSet = {}, {}
        for ch in s:
            n = sSet.get(ch) if sSet.get(ch) != None else 0
            sSet.update({ch:(n+1)})
        for ch in t:
            n = tSet.get(ch) if tSet.get(ch) != None else 0
            tSet.update({ch:(n+1)})
        if sSet == tSet:
            return True
        else:
            return False
        