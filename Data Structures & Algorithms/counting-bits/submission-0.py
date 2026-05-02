class Solution:
    def count(self, n:int) -> int:
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1 # same as n // 2
        return count

    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n+1):
            bits = self.count(i)
            result.append(bits)
        
        return result