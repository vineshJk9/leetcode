class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(points)):
            if i==len(points)-1:continue
            count+=max(abs(points[i+1][0]-points[i][0]),abs(points[i+1][1]-points[i][1]))

s = Solution()
print(s.minTimeToVisitAllPoints([[3,2],[-2,2]]))