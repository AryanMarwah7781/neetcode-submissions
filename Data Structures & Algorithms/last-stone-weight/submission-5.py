class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[]
        max_heap=[-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            max_1=heapq.heappop(max_heap)
            max_2=heapq.heappop(max_heap)
            print("Max_1 : "+ str(max_1))
            print("Max_2 : "+ str(max_2))
            if max_1==max_2:
                continue
            else:
                max_diff=abs(max_1)-abs(max_2)
                heapq.heappush(max_heap,-max_diff)
        if len(max_heap) == 1:
            return abs(max_heap[0])
        else:
            return 0


        