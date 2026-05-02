class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = len(nums)
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(res - 1):
            if (nums[i] + 1) != nums[i+1]:
                return nums[i] + 1
        return res