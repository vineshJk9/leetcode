class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in s:
                return [s[c], i]
            s[num] = i

s = Solution()
print(s.twoSum([2,7,11,15], 9))
        