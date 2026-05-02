class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        dict1=dict()
        dict1["{"]="}"
        dict1["("]=")"
        dict1["["]="]"
        stack=[]
        
        for x in s:
            if x in dict1:  # Opening bracket
                stack.append(x)
            elif x in dict1.values():  # Closing bracket
                if len(stack)==0:  # Stack empty but found closing bracket
                    return False
                val=stack[-1]
                if dict1[val] != x:  # Check if matches corresponding opening bracket
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0  # Ensure all brackets were matched