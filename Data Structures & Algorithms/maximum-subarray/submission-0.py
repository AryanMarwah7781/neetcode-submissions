class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=nums[0]
        max_sum=nums[0]
        for x in nums[1:]:
            curr_sum=max(x,curr_sum+x)
            max_sum=max(curr_sum,max_sum)
        return max_sum




        