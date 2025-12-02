class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        d = {}
        q = []
        for i in coins:
            if amount - i >=0:
                d[amount-i] = 1
                q.append(amount-i)
        while(len(q)):
           k = q.pop(0)
           for i in coins:
               v = k - i
               if v>=0 and v in d:
                   if d[v] > d[k] + 1:
                       d[v] = d[k] + 1
               elif v >=0:
                   d[v] = d[k] + 1
                   q.append(v)
        if 0 in d:
            return d[0]
                   
        return -1

        
s = Solution()
print(s.coinChange([5,306,188,467,494], 7047))