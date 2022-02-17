## In share trading, a buyer buys shares and sells on a future date.
## Given the stock price of n days, the trader is allowed to make at most k transactions, where a new transaction can only start after the previous transaction is complete.
##  find out the maximum profit that a share trader could have made. 

# Dynamic Programming

def maxProfitWithKTrans(prices, k):
  if not len(prices):
    return 0
  profits = [[0 for d in prices] for t in range(k+1)]

  for t in range(1, k+1):
    maxSoFar = float('-inf')
    for d in range(1, len(prices)):
      maxSoFar = max(maxSoFar, profits[t-1][d-1] - prices[d-1])
      profits[t][d] = max(profits[t][d-1], maxSoFar + prices[d])
  return profits[-1][-1]

prices = [5,11,3,50,60,90]
k = 2
maxProfitWithKTrans(prices, k)