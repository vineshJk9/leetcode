class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for _ in range(32):
            res = res << 1
            if n:
                res = res | n & 1
                n = n >> 1
        return res
      
s = Solution()
print(s.reverseBits(43261596))