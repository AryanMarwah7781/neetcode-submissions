class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1
        
        new = sorted(frequency.items(), key = lambda x: x[1], reverse = True)
        print(new)
        result = []
        for i in range(k):
            result.append(new[i][0])

        return result