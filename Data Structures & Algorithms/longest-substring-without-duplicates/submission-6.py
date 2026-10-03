class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        max_l=0
        seen=set()
        while r<len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l=l+1
            else:
                seen.add(s[r])
                r= r+1
            max_l=max(max_l,(r-l))
        return max_l