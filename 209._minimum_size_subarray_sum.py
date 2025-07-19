class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        j=0
        l=float('inf')
        for i in range(len(nums)):
            sum = sum + nums[i]
            while sum >= target:
                l = min(l,(i-j)+1)
                sum = sum - nums[j]
                j=j+1
        if l == float('inf'):
            return 0
        return l

s = Solution()
print(s.minSubArrayLen(7,[2,3,1,2,4,3]))