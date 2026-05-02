class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        curr = []
        def dfs(i):
            if i >= len(nums):
                # consequent pop() would remove curr, therefore curr.copy()
                subsets.append(curr.copy())
                return

            # include the current number
            curr.append(nums[i])
            print(curr)
            dfs(i + 1)
            curr.pop()

            # do not include the current number
            dfs(i + 1)
        
        dfs(0)
        return subsets