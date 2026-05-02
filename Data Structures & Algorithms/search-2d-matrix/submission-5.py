class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row_1 = []
        end = len(matrix[0]) - 1

        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][end]:
                row_1 = matrix[i]
                break  # optional: stop once you’ve found the first matching row
        if not row_1:
            return False
        l=0
        r=end
        while l<=r:
            m=(l+r)//2
            print(m)
            if row_1[m]==target:
                return True
            if target<=row_1[m]:
                r=m-1
            else:
                l=m+1
        return False


        