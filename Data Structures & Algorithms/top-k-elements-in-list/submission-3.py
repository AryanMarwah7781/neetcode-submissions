class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list_ret=[]
        dict_tool={}
        for num in nums:
            if num in dict_tool:
                temp=dict_tool[num]
                dict_tool[num]=(temp+1)
            else:
                dict_tool[num]=1
        sorted_dict_desc = dict(sorted(dict_tool.items(), key=lambda dict_tool: dict_tool[1], reverse=True))
        list_1=list(sorted_dict_desc.keys())
        return list_1[0:k]


        