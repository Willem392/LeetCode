class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        for i in nums:
            target = -i
            tempNums = [*nums]
            tempNums.remove(i)
            s2 = set()
            for j in range(len(tempNums)):
                if target - tempNums[j] in s2:
                    s.add(tuple(sorted([-target, target - tempNums[j], tempNums[j]])))
                s2.add(tempNums[j])
        l = []
        for elem in s:
            l.append([*elem])
        return l