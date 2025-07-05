class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums:
            nums[abs(i)-1] = abs(nums[abs(i)-1]) * -1
        for idx, num in enumerate(nums):
            if num > 0:
                result.append(idx+1)
        return result
                
            
        
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))