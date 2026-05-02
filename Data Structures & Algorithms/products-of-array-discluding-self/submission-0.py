class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_orig=1
        product_orig_without_0=1
        zero_counter=0
        for i in range(0,len(nums)):
            if nums[i]==0:
                product_orig=0
                zero_counter= zero_counter+1
                continue
            product_orig_without_0*=nums[i]
        list1=[]
        for num in nums:
            if num==0 and zero_counter==1:
                list1.append(product_orig_without_0)
                continue
            if num==0 and zero_counter>1:
                list1.append(0)
                continue
            if num is not 0 and zero_counter>=1:
                list1.append(0)
                continue
            list1.append(int(product_orig_without_0/num))
        
        return list1



            





        