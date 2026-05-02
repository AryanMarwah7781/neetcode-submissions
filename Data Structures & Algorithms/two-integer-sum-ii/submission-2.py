class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        list1=[]
        for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j] == target:
                    list1.append(i+1)
                    list1.append(j+1)
                    print(list1)
                    return list1


    
        