class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subArrays = 0
        print(len(arr) - k + 1)
        for l in range(0, len(arr) - k + 1):
            print(arr[l:l+k])
            value = sum(arr[l:l+k])
            ave = value/k
            if ave >= threshold:
                subArrays += 1

        return subArrays