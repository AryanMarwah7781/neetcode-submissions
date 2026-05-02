class Solution:
    def climbStairs(self, n: int) -> int:
        
        def stairsCounter(l: int, cache: dict):

            if l <= 2:
                return l
            if l in cache:
                return cache[l]

            first = stairsCounter(l-1, cache)
            second = stairsCounter(l-2, cache)

            cache[l-2] = second
            cache[l-1] = first
            
            return first + second
        
        return stairsCounter(n, {})