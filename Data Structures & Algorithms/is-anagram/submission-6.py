class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        s_dict={}
        t_dict={}
        for l in s:
            if l in s_dict:
                temp=s_dict[l]
                temp=temp+1
                s_dict[l]=temp
            else:
                s_dict[l]=1
        for y in t:
            if y in s_dict:
                temp=s_dict[y]
                temp=temp-1
                s_dict[y]=temp
            else:
                return False
        for key,val in s_dict.items():
            if val!=0:
                return False
        return True


        
        