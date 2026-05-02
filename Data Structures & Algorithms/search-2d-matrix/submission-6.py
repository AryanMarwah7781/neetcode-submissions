class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top=0
        bottom=len(matrix)-1
        l=0
        r=len(matrix[0])-1
        target_row=-1999
        while top<=bottom:
            mid=(top+bottom)//2
            if target>matrix[mid][r]:
                top=mid+1
            elif target<matrix[mid][l]:
                bottom=mid-1
            else:
                target_row=mid
                break
        if target_row==-1999:
            return False
        while l<=r:
            target_mid=l+(r-l)//2
            if target==matrix[target_row][target_mid]:
                return True
            elif target>matrix[target_row][target_mid]:
                l=target_mid+1
            else:
                r=target_mid-1
        return False



        