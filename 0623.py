# def stoneGame(piles):
#     n = len(piles)
#     dp = [[[0 for i in range(2)]for j in range(n)]for k in range(n)]
#     for i in range(n):
#         dp[i][i][0] = piles[i]
#         dp[i][i][1] = 0
#
#     for l in range(1,n):
#         for i in range(n-l):
#             j = i + l
#             left = dp[i+1][j][1] + piles[i]
#             right = dp[i][j-1][1] + piles[j]
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
#         dp[i] = dp[i-1]+1
#         for j in range(2,i):
#             dp[i] = max(dp[i],dp[j-2]*(i-j+1))
#     return dp[N-1]
# N = 9
# print(maxA(N))

# def LIS(nums):
#     n = len(nums)
#     dp = [1 for i in range(n)]
#     for i in range(n):
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 dp[i] = max(dp[i],dp[j]+1)
#     return max(dp)
#
# piles = [1,3,4,5,3,6,2,5]
# print(LIS(piles))

# def coinChange(coins,target):
#     dp = [target+1 for i in range(target+1)]
#     dp[0] = 0
#     for i in range(1,target+1):
#         for coin in coins:
#             if i - coin >= 0:
#                 dp[i] = min(dp[i-coin]+1,dp[i])
#     return dp[target]
# coins = [1,2,5]
# amount = 13
# print(coinChange(coins,amount))

def LCS(str1,str2):
    m,n = len(str1),len(str2)
    dp = [[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
str1 = 'abc'
str2 = 'eiwdlatbldc'
print(LCS(str1,str2))

# def LCS(str1,str2):
#     m,n = len(str1),len(str2)
#     dp = [[0 for i in range(n+1)]for j in range(m+1)]
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if str1[i-1] == str2[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
#     return dp[m][n]
# str1 = 'abc'
# str2 = 'eiwdlatbldc'
# print(LCS(str1,str2))
# ans = 3


