class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_numb_freq={}
        list1=[]
        for i in nums:
            if i in dict_numb_freq:
                temp=dict_numb_freq[i]
                dict_numb_freq[i]=temp+1
            else:
                dict_numb_freq[i] = 1
        sorted_dict = dict(sorted(dict_numb_freq.items(), key=lambda item: item[1], reverse=True))
        flag = k
        for key, val in sorted_dict.items():
            if flag>0:
                list1.append(key)  # use append() for lists, not add()
            flag = flag -1
        return list1
        
        