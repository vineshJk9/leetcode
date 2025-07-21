class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        x = 1
        for _ in range(32):
            if x & n:
                count = count + 1
            x = x * 2
        return count

s = Solution()
print(s.hammingWeight(2147483645))