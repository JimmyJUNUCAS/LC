# def stoneGame(piles):
#     n = len(piles)
#     dp = [[[0 for i in range(2)]for _ in range(n)]for j in range(n)]
#     for i in range(n):
#         dp[i][i][0] = piles[i]
#
#     for l in range(1,n):
#         for i in range(n-l):
#             j = l + i
#             left = piles[i] + dp[i+1][j][1]
#             right = piles[j] + dp[i][j-1][1]
#             if left > right:
#                 dp[i][j][0] = left
#                 dp[i][j][1] = dp[i+1][j][0]
#             else:
#                 dp[i][j][0] = right
#                 dp[i][j][1] = dp[i][j-1][0]
#     return dp[0][n-1][0] - dp[0][n-1][1]
# piles = [10,3,4]
# print(stoneGame(piles))
#
# def maxA(N):
#     dp = [0 for i in range(N)]
#     for i in range(N):
#         dp[i] = dp[i-1] + 1
#         for j in range(2,i):
#             dp[i] = max(dp[i],dp[j-2]*(i-j+1))
#     return dp[N-1]
# N = 9
# print(maxA(N))
#
# def LIS(nums):
#     n = len(nums)
#     dp = [1 for i in range(n)]
#     for i in range(n):
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 dp[i] = max(dp[i],dp[j]+1)
#     return max(dp)
# piles = [1,3,4,5,3,6,2,5]
# print(LIS(piles))
#
# def coinChange(nums,amount):
#     n = len(nums)
#     dp = [amount+1 for i in range(amount+1)]
#     dp[0] = 0
#     for i in range(amount+1):
#         for coin in nums:
#             if i - coin < 0:
#                 continue
#             dp[i] = min(dp[i],dp[i-coin]+1)
#     return dp[amount]
# coins = [1,2,5]
# amount = 13
# print(coinChange(coins,amount))
#
# def maxProfit(nums):
#     n = len(nums)
#     dp = [[0 for i in range(2)]for j in range(n+1)]
#     dp[0][1] = -nums[0]
#     for i in range(1,n+1):
#         dp[i][0] = max(dp[i-1][0],dp[i-1][1]+nums[i-1])
#         dp[i][1] = max(dp[i-1][1],-nums[i-1])
#     return dp[n][0]
# prices = [2,3,6,-1,5,4]
# print(maxProfit(prices))
#
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

def maxProfit_fee(nums,fee):
    n = len(nums)
    dp = [[0 for i in range(2)]for j in range(n)]
    dp[0][1] = -nums[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+nums[i])
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-nums[i]-fee)
    return dp[n-1][0]
prices = [2,3,6,-1,5,4]
fee = 2
print(maxProfit_fee(prices,fee))

def maxProfit_k(nums,K):
    n = len(nums)
    if K > n/2:
        return maxProfit_inf(nums)
    dp = [[[0 for i in range(2)]for k in range(K+1)]for j in range(n+1)]
    for i in range(K):
        dp[0][i][1] = -nums[0]

    for i in range(1,n):
        for k in range(K):
            dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+nums[i])
            dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-nums[i])
    return dp[n-1][K-1][0]
prices = [2,3,6,-1,5,4]
fee = 1
print(maxProfit_k(prices,fee))

def LPS(s):
    n = len(s)
    dp = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] +2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
    return dp[0][n-1]
s = 'aba'
print(LPS(s))


