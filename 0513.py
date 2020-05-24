def maxProfit(nums):
    n = len(nums)
    dp = [[0 for i in range(2)]for j in range(n)]
    dp[0][1] = -nums[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+nums[i])
        dp[i][1] = max(dp[i-1][1],-nums[i])
    return dp[n-1][0]
prices = [2,3,6,-1,5,4]
print(maxProfit(prices))

def maxProfit_inf(nums):
    n = len(nums)
    dp = [[0 for i in range(2)]for j in range(n)]
    dp[0][1] = -nums[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+nums[i])
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-nums[i])
    return dp[n-1][0]
prices = [2,3,6,-1,5,4]
print(maxProfit_inf(prices))

def maxProfit_cold(nums):
    n = len(nums)
    dp = [[0 for i in range(2)]for j in range(n)]
    dp[0][1] = -nums[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+nums[i])
        dp[i][1] = max(dp[i-1][1],dp[i-2][0]-nums[i])
    return dp[n-1][0]
prices = [2,3,6,-1,5,4]
print(maxProfit_cold(prices))

def maxProfit_fee(nums,k):
    n = len(nums)
    dp = [[0 for i in range(2)]for j in range(n)]
    dp[0][1] = -nums[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+nums[i])
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-nums[i]-k)
    return dp[n-1][0]
prices = [2,3,6,-1,5,4]
print(maxProfit_fee(prices,2))

def maxProfit_2(nums):
    n = len(nums)
    dp = [[[0 for i in range(2)]for _ in range(2)]for j in range(n)]
    dp[0][0][1] = dp[0][1][1] = -nums[0]
    for i in range(1,n):
        for k in range(2):
            dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+nums[i])
            dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-nums[i])
    return dp[n-1][1][0]
prices = [2,3,6,-1,5,4]
print(maxProfit_2(prices))

def maxProfit_k(nums,K):
    n = len(nums)
    if K > n/2:
        return maxProfit_inf(nums)
    dp = [[[0 for i in range(2)]for j in range(K+1)]for _ in range(n+1)]
    for k in range(K):
        dp[0][k][1] = -nums[k]
    for i in range(1,n):
        for k in range(K):
            dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+nums[i])
            dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-nums[i])
    return dp[n-1][K-1][0]
prices = [2,3,6,-1,5,4]
print(maxProfit_k(prices,1))

def coinChange(coins,amount):
    dp = [amount+1 for i in range(amount+1)]
    dp[0] = 0
    for i in range(amount+1):
        for coin in coins:
            if i - coin < 0 : continue
            dp[i] = min(dp[i],dp[i-coin]+1)
    return dp[amount]
coins = [1,2,5]
amount = 13
print(coinChange(coins,amount))