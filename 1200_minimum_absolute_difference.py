class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = float('inf')
        abs_dif = []
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] < min_diff:
                abs_dif = [[arr[i-1], arr[i]]]
                min_diff = arr[i] - arr[i-1]
            elif arr[i] - arr[i-1] == min_diff:
                abs_dif.append([arr[i-1], arr[i]])
        return abs_dif

s = Solution()
print(s.minimumAbsDifference([4,2,1,3]))