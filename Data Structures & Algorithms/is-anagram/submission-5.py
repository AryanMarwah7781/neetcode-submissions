class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sortedS, sortedT = {}, {}
        for i in range(len(s)):
            sortedS[s[i]] = 1 + sortedS.get(s[i], 0)
            sortedT[t[i]] = 1 + sortedT.get(t[i], 0)
        return sortedS == sortedT