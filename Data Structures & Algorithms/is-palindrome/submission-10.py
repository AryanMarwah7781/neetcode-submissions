class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(char for char in s if char.isalnum())
        print(result)
        len_s=len(result)
        result=result.lower()
        for i in range(len(result)):
            if result[i]!=result[len_s-i-1]:
                return False
        return True 
                
        