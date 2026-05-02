class Solution:
    # area calculation 
    #area=min(height[l],height[r])*(l-r)
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        def area(height,breadth):
            return height * breadth
        max_area=0
        while l<=r:
            area=min(height[l],height[r])*abs(l-r)
            max_area=max(area,max_area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
            


        