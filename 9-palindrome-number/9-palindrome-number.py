class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        backwards = str(x)[::-1]
        for i in range(0, int(len(backwards)/2)):
            if str(x)[i] != backwards[i]:
                return False
        return True
