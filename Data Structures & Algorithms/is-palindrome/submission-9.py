class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        cleaned_string = re.sub(r'[^a-zA-Z]', '', s)
        cleaned = re.sub(r'[^a-z0-9]', '', s)
        s=list(cleaned)
        l=0
        r=len(s)-1
        print(len(s))
        print(r)
        while l<r:
            if s[l]!=s[r]:
                return False 
            r=r-1
            l=l+1
        return True