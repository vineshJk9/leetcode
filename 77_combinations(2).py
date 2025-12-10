class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []
        curr = []

        def backtrack(start):
            # If we have k numbers, add a copy
            if len(curr) == k:
                res.append(curr[:])
                return

            # Try each number from start..n
            for num in range(start, n + 1):
                curr.append(num)
                backtrack(num + 1)
                curr.pop()

        backtrack(1)
        return res
    
s = Solution()
n = 5
k = 3
print(s.combine(n, k))