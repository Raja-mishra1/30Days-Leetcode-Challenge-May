class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = [(math.sqrt(point[0]**2 + point[1]**2),point) for point in points]
        return[point for distance,point in sorted(dist)[:K]]
