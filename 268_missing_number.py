class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0 
        for i in nums:
            sum = sum + i
        return int((len(nums)*(len(nums)+1))/2 - sum )

s = Solution()
print(s.missingNumber([0,1]))