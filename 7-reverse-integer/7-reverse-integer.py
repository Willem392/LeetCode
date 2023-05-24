class Solution:
    def reverse(self, x: int) -> int:
        numString = str(x)[::-1]
        if '-' in numString:
            numString = numString.replace('-', '')
            numString = '-' + numString
        if int(numString) > (2**31)-1 or int(numString) < -2**31:
            return 0
        return int(numString)