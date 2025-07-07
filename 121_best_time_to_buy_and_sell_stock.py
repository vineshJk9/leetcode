class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        r = 1
        l = 0
        m_profit = 0
        while r != len(prices):
            if prices[l] < prices[r]:
                m_profit = max(m_profit, prices[r]-prices[l])
            else:
                l=r
            r=r+1
        return m_profit

s = Solution()
print(s.maxProfit([1,2,4,2,5,7,2,4,9,0,9]))
        