class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for n in nums:
            frequency[n] = 1 + frequency.get(n,0)
        
        new = sorted(frequency.items(), key = lambda x: x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(new[i][0])

        return result