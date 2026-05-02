class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff=defaultdict(int)
        for index,num in enumerate(nums):
            difference=target-num
            print(difference)
            if difference in diff.keys():
                print("Coming here")
                return [diff[difference],index]
            diff[num]=index
            print(diff)
        return [0,0]
            
        