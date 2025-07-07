class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        if nums[0] >=0:
            return [num**2 for num in nums]
        
        m=len(nums)
        for i in range(len(nums)):
            if nums[i]>=0:
                m=i
                break
        i=m-1
        res = []
        while True:
            if i==-1:
                res.extend([x**2 for x in nums[m:]])
                break
            if m==len(nums):
                res.extend([x**2 for x in nums[:i+1][::-1]])
                break
            if abs(nums[i]) < nums[m]:
                res.append(nums[i]**2)
                i=i-1
            else:
                res.append(nums[m]**2) 
                m=m+1
        return res
        


s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
# [-4,-1]
# [-4,-1,0]
#[-4,-1,0,3]