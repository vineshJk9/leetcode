class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False


s = Solution()
print(s.containsDuplicate([1,2,3]))
        