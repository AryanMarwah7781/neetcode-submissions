class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for s in strs:
            sorted_string = ''.join(sorted(s))
            if sorted_string in dict1:
                arr=dict1[sorted_string]
                arr.append(s)
            else:
                dict1[sorted_string]=[s]
        return list(dict1.values())

            





        