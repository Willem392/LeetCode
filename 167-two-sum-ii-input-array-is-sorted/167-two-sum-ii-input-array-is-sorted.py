class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(numbers)):
            if target - numbers[i] in s:
                return [s.get(target - numbers[i])+1, i+1]
            s.update({numbers[i]: i})