class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i, n in enumerate(nums):
            if (target - n) in diff:
                return [diff[target-n], i]
            diff[n] = i

        return []