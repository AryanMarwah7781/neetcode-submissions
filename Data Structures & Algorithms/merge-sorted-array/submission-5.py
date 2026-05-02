class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        one = m-1
        two = n-1
        sort = len(nums1) - 1

        while one >= 0 and two >= 0:
            print(nums1)
            if nums1[one] < nums2[two]:
                nums1[sort] = nums2[two]
                two -= 1
            else: #nums1 >= nums2
                nums1[sort] = nums1[one]
                one -= 1
            sort -= 1

        if two >= 0:
            print('messed it')
            nums1[0:sort+1] = nums2[0:two+1]        

