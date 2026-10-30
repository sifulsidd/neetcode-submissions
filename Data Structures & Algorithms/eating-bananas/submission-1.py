class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed,maxSpeed = 1, max(piles)
        res = maxSpeed
        while minSpeed <= maxSpeed:
            speed = (minSpeed + maxSpeed) // 2
            time = 0
            for num in piles:
                time += math.ceil(float(num)/speed)
            if time <= h:
                res = min(speed, res)
                maxSpeed = speed - 1
            else:
                minSpeed = speed + 1
        return res