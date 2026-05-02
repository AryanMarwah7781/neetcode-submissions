class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        # XOR same 2 numbers == 0 - since they cancel each other out
        # 
        for n in nums:
            result = n ^ result
        return result