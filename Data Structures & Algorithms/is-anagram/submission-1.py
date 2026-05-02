class Solution:
    def sort_string(string):
        return ''.join(sorted(string))

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_s=''.join(sorted(s))
        sorted_t=''.join(sorted(t))
        if sorted_s == sorted_t:
            return True 
        else:
            return False
        # dict_t={}
        # dict_s={}
        # for char in s:
        #     if char in dict_t:
        #         temp=dict_t[char]
        #         dict_t[char]=(temp+1)
        #     else:
        #         dict_t[char]=1
        




        