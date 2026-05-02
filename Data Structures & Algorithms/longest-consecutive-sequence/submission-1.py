class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(set(nums))
        nums_sorted_arr = [0 for _ in range(len(nums_sorted))]
        for i in range(1,len(nums_sorted)):
            nums_sorted_arr[i]=nums_sorted[i]-nums_sorted[i-1]
        print(nums_sorted_arr)
        if len(nums)==0:
            return 0
        def max_consecutive_ones(arr):
            # build a "01" string, split on '0' to isolate runs of '1', then take the longest
            runs = ''.join('1' if x == 1 else '0' for x in arr).split('0')
            return max((len(r) for r in runs), default=0)
        return 1+max_consecutive_ones(nums_sorted_arr)



        
        