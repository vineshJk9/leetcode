class Solution(object):
    l = []
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = []
        self.backtrack(nums, 0, [])
        return self.l

    def backtrack(self, nums, n, result):
        self.l.append(result)
        for i in range(n, len(nums)):
            self.backtrack(nums, i+1,result + [nums[i]])


s = Solution()
print(s.subsets([1,2,3]))