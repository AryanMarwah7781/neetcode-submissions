class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        k={}
        max_l=0
        while r<len(s):
            if s[r] not in k:
                k[s[r]]=1
                r+=1
            else:
                del(k[s[l]])
                l+=1
            max_l=max(max_l,r-l)
        return max_l
            
        

        
        