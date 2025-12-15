class Solution(object):
    l = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = []
        self.rec(nums,0,len(nums))
        return self.l
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp  
        return nums
    def rec(self, nums, k, n):
        if nums not in self.l:
            self.l.append(nums.copy())
        for i in range(k, n):
            for j in range(i+1, n):
                nums = self.swap(nums,i,j)
                self.rec(nums,i+1,n)
                nums = self.swap(nums,j,i)
                 
s = Solution()
nums = [1,2,3,4]
print(len(s.permute(nums)))