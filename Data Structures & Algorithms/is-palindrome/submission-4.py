import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Clean and normalize the string
        # Combine lowercasing and cleaning into one string variable
        s_lower = s.lower()
        
        # NOTE: Your original regex r'[^a-zA-Z]' only keeps letters.
        # This standard solution usually requires alphanumeric (letters and numbers):
        cleaned_string = re.sub(r'[^a-z0-9]', '', s_lower)
        
        # 2. Initialize Two Pointers
        l = 0
        r = len(cleaned_string) - 1
        
        # 3. Two-Pointer Check (using the standard l < r condition)
        while l < r:
            # Compare characters
            if cleaned_string[l] != cleaned_string[r]:
                return False 
            
            # Move pointers inward
            r -= 1
            l += 1
            
        return True