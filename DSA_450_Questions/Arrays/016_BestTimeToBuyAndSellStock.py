## You are given an array prices where prices[i] is the price of a given stock on the ith day.
## You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
## Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

# Simple solution

class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, A, n):
	    ans=[]
        for i in range(1,n):
            if(A[i]>A[i-1]):
                ans.append([i-1,i])
        return ans

# Sliding Window

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left = buy, right = sell
        l , r = 0, 1
        maxProfit = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
            
        return maxProfit
        