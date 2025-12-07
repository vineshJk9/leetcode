class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return 0
        i = 0
        currSum = 0
        maxSum = nums[0]
        while i < len(nums) and nums[i] <= 0:
            if nums[i] > maxSum:
                maxSum = nums[i]
            i=i+1
        for j in range(i, len(nums)):
            if nums[j] + currSum < 0:
                currSum = 0
            else:
                currSum = currSum + nums[j]
            if currSum > maxSum:
                maxSum = currSum
        return maxSum
        
        
s = Solution()
print(s.maxSubArray([-2,-1]))