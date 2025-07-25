class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums) - 1
            while left<right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left]==nums[left+1]:
                        left = left+1
                    while left < right and nums[right]==nums[right-1]:
                        right = right-1
                    
                    left = left+1
                    right = right-1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
    
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
        