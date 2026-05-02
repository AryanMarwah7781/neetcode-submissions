class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # want to get the bit in the ith position to the one position before &
            bit = (n >> i) & 1
            # adding the bit to the 31-i (flip) position
            res += (bit << (31 - i))

        return res