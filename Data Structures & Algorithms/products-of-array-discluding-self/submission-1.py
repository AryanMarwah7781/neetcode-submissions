class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        for n in nums:
            if n != 0:
                product *= n
            else:
                zero += 1
        
        result = []
        for i in range(len(nums)):
            if zero > 0:
                if zero == 1:
                    if nums[i] == 0:
                        result.append(product)
                    else: 
                        result.append(0)
                elif zero >= 2:
                    result.append(0)
            else:
                result.append(product//nums[i])

        return result