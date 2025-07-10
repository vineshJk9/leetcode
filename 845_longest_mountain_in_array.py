class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) <3:
            return 0
        increasing = 1
        max_value = 0
        count = 1
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] >0:
                if increasing == 1:
                    count =count+1
                else:
                    count = 2
                    increasing = 1
            elif arr[i] - arr[i-1] < 0:
                if increasing == 1 and count==1:
                    count=1
                    continue
                increasing = 0
                count=count+1
                max_value = max(max_value, count)
            else:
                count = 1
                increasing = 1
        return max_value
        
s = Solution()
print(s.longestMountain([1,2,3,2,3,4,5,4,3,2,1]))
