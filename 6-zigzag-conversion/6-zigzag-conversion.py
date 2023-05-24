class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lists = []
        for i in range (0, numRows):
            lists.append([])
        index = 0
        direction = 1
        for ch in s:
            lists[index].append(ch)
            if numRows is not 1:
                index += direction
                if index is 0 or index == numRows-1:
                    direction *= -1
        finalString = ""
        for i in range(0, numRows):
            for j in lists[i]:
                finalString += j
        return finalString
        