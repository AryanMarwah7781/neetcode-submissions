class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temp=[]
        left=0
        right = len(numbers)-1
        while right>left:
            sum1= numbers[right]+numbers[left]
            if sum1== target:
                temp.append(left+1)
                temp.append(right+1)
                return temp
            elif sum1>target:
                right-=1
            else:
                left+=1


    
        