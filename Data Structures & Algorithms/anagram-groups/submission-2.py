class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            anagram = ''.join(sorted(word))
            if anagram in groups:
                groups[anagram].append(word)
            else:
                groups[anagram] = [word]
        
        return list(groups.values())