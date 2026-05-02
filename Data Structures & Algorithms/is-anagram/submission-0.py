class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp="".join(sorted(s))
        sorted_string = ''.join(sorted(t))
        return temp == sorted_string
            

        
        