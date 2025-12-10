class Solution(object):
    l = []
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.l = []
        self.rec(n, k, 0, [], 0)
        return self.l

    def rec(self, n, k, i, l1, index):
        if i==0 and (n-index)<k:
            return
        if i == 0:
            l1 = []
        if k==i:
            self.l.append(l1)
            return
        
        
        for j in range(index, n):
            self.rec(n, k, i+1, l1+[j+1], j+1)
        

s = Solution()
n = 5
k = 3
print(s.combine(n, k))