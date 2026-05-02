class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for r in range(len(nums)):
            if nums[r] in seen:
                print(f"checking duplicate at index: {seen[nums[r]]}") 
                if abs(seen[nums[r]] - r) <= k:
                    return True
                # else:
                #     nums[r] = r
            seen[nums[r]] = r
        
        return False
            