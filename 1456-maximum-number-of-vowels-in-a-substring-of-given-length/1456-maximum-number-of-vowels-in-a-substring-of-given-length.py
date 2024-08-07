class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def v(c):
            return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'
        maxCount, count, left, right = 0, 0, 0, -1
        while right < k - 1:
            right += 1
            if v(s[right]):
                count += 1
            maxCount = max(maxCount, count)
        while right < len(s) - 1:
            right += 1
            if v(s[right]):
                count += 1
            if v(s[left]):
                count -= 1
            left += 1
            maxCount = max(maxCount, count)
        return maxCount