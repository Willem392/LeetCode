class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortestString = 201
        for string in strs:
            shortestString = min(shortestString, len(string))
        notSimilarIndex = shortestString
        for i in range(0, shortestString):
            if(notSimilarIndex != shortestString):
                break
            for j in range(1, len(strs)):
                if strs[j-1][i] != strs[j][i]:
                    print("yea")
                    notSimilarIndex = i
                    break
        return strs[0][0:notSimilarIndex]
        