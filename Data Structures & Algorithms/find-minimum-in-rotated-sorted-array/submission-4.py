class Solution:
    def findMin(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        while l<r:
            mid = (l+r)//2
            if arr[r]<arr[mid]:
                l=mid+1
            elif arr[r]>arr[mid]:
                r=mid
        return arr[l]
        