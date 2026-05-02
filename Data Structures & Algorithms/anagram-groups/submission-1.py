class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted_chars = sorted(string)
        # sorted_string = "".join(sorted_chars)
        dict1={}
        for string in strs:
            sorted_chars = sorted(string)
            sorted_string = "".join(sorted_chars)
            if sorted_string in dict1:
                temp=dict1[sorted_string]
                temp=temp.append(string)
            else:
                dict1[sorted_string]=[string]
        return dict1.values()



        