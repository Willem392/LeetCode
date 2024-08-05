class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        valid_count = 0
        i = 1
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        while i  < len(flowerbed) - 1:
            if flowerbed[i] == 0:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    valid_count += 1
                    i += 1
            i += 1
        return valid_count >= n