class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for i in digits:
            string += str(i)
        ret = []
        for ch in str(int(string) + 1):
            ret.append(int(ch))
        return ret