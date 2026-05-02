import math, heapq
from typing import List, Tuple

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap: List[Tuple[float, Tuple[int,int]]] = []
        for r, c in points:
            d = math.hypot(r, c)
            heapq.heappush(heap, (d, (r, c)))

        result = []
        for _ in range(k):
            dist, pt = heapq.heappop(heap)
            result.append(pt)
        return result
