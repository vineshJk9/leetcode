class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
s = Solution()
print(s.coinChange([5,306,188,467,494], 7047))