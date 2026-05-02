class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_s=list(s)
        l=0
        r=0
        max_str=0
        set1=set()
        while r<len(s):
            if list_s[r] not in set1:
                set1.add(list_s[r])
                r+=1
                max_str = max(max_str, abs(l-r))
            else:
                set1.remove(list_s[l])
                l+=1
        return max_str



            
        return max_str



        
        
        