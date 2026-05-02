class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=''.join(char for char in s if char.isalnum())
        palindrome_s=str(s[::-1])
        clean_text = ''.join(char for char in palindrome_s if char.isalnum())
        print(clean_text)
        return clean_text==s
        