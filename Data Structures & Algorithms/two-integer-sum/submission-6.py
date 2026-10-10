
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        # Pass 1: Populate the hash map
        for i in range(len(nums)):
            dict1[nums[i]] = i
            
        # Pass 2: Find the complement
        for i in range(len(nums)):
            diff = target - nums[i]  # Bug 1 Fixed: use nums[i], not i
            
            # Bug 2 Fixed: Ensure we don't use the exact same element twice
            if diff in dict1 and dict1[diff] != i:
                # Bug 3 Fixed: Avoid using .sort() which returns None
                return [i, dict1[diff]]
     