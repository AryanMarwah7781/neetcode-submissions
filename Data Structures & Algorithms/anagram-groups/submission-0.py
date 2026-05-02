class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for s in strs:
            # Sort the string to create the key
            sorted_str = ''.join(sorted(s))
            
            # If key exists, append to its list, else create a new list
            if sorted_str in anagram_map:
                anagram_map[sorted_str].append(s)
            else:
                anagram_map[sorted_str] = [s]
        
        # Return the grouped anagrams
        return list(anagram_map.values())



            
        