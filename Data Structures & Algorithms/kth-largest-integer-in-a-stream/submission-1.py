class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        heapq.heapify(self.nums)
        elements_wanted_list=len(self.nums)-k
        for i in range(0,elements_wanted_list):
            heapq.heappop(self.nums)
        print(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums)!=0:
            smallest_element=self.nums[0]
        else:
            smallest_element=-1001
        if len(self.nums)<self.k:
            heapq.heappush(self.nums,val)
        else:
            if smallest_element<val:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums,val)
        smallest_element=self.nums[0]
        return smallest_element

        


        
