class Solution:
    def distance_squared(self,point):
        x, y = point
        return x**2 + y**2  # Skip the sqrt!
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        outer_self=self
        class closestPoint:
            def __init__(self,point:List[int]):
                self.point=point
                self.distance=outer_self.distance_squared(self.point)
            def __lt__(self,other):
                return self.distance<other.distance
        point_final=[closestPoint(point) for point in points]
        heapq.heapify(point_final)
        return [heapq.heappop(point_final).point for _ in range(k)]


        