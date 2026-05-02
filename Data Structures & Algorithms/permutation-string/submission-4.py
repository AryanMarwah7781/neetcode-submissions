class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)
        a_sort=sorted(s1)
        def match_permut(s1_m,s2_m):
            b=sorted(s2_m)
            return s1_m==b
        while r<=len(s2):
            s2_m=s2[l:r]
            matc=match_permut(a_sort,s2_m)
            if matc:
                return True
            else:
                l=l+1
                r=r+1
        return False