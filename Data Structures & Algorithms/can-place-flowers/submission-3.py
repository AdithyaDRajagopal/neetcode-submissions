class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            count += 1

        if len(flowerbed) >= 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            count += 1

        if len(flowerbed) >= 2 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            count += 1
            
        for i in range(0, len(flowerbed) - 1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                count += 1
                flowerbed[i] = 1
            
            if count >= n:
                return True
        
        return count >= n