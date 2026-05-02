class Solution:
    def search(self, nums: List[int], k: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            m = l + (h - l) // 2
            if nums[m] == k:
                return m
            elif nums[m] < k:
                l = m + 1
            else:
                h = m - 1
        return -1
