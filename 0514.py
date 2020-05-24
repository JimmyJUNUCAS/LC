# def maxProfit_inf(nums):
#     n = len(nums)
#     dp = [[0 for i in range(2)]for j in range(n+1)]
#     dp[0][1] = -nums[0]
#     for i in range(1,n+1):
#         dp[i][0] = max(dp[i-1][0],dp[i-1][1]+nums[i-1])
#         dp[i][1] = max(dp[i-1][1],dp[i-1][0]-nums[i-1])
#     return dp[n][0]
# prices = [2,3,6,-1,5,4]
# print(maxProfit_inf(prices))
#
# def maxProfit_cold(nums):
#     n = len(nums)
#     dp = [[0 for i in range(2)]for j in range(n+1)]
#     dp[0][1] = -nums[0]
#     for i in range(1,n+1):
#         dp[i][0] = max(dp[i-1][0],dp[i-1][1]+nums[i-1])
#         dp[i][1] = max(dp[i-1][1],dp[i-2][0]-nums[i-1])
#     return dp[n-1][0]
# prices = [2,3,6,-1,5,4]
# print(maxProfit_cold(prices))
#
# def maxProfit_fee(nums,fee):
#     n = len(nums)
#     dp = [[0 for i in range(2)]for j in range(n+1)]
#     dp[0][1] = -nums[0]
#     for i in range(1,n+1):
#         dp[i][0] = max(dp[i-1][0],dp[i-1][1]+nums[i-1])
#         dp[i][1] = max(dp[i-1][1],dp[i-1][0]-nums[i-1]-fee)
#     return dp[n-1][0]
# prices = [2,3,6,-1,5,4]
# print(maxProfit_fee(prices,3))
#
# def maxProfit_2(nums):
#     n = len(nums)
#     dp = [[[0 for i in range(2)]for j in range(2)]for _ in range(n+1)]
#     dp[0][0][1] = dp[0][1][1] = -nums[0]
#     for i in range(1,n+1):
#         for k in range(2):
#             dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+nums[i-1])
#             dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-nums[i-1])
#     return dp[n][1][0]
# prices = [2,3,6,-1,5,4]
# print(maxProfit_2(prices))
#
# def maxProfit_k(nums,K):
#     n = len(nums)
#     if K > n/2:
#        return maxProfit_inf(nums)
#     dp = [[[0 for i in range(2)]for j in range(K+1)]for _ in range(n+1)]
#     for k in range(K+1):
#         dp[0][k][1] = -nums[0]
#     for i in range(1,n+1):
#         for k in range(1,K+1):
#             dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+nums[i-1])
#             dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-nums[i-1])
#     return dp[n][K][0]
#
# prices = [2,3,6,-1,5,4]
# print(maxProfit_k(prices,1))
#
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
#
# def minDistance(str1,str2):
#     m, n = len(str1), len(str2)
#     dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],dp[i-1][j-1])+1
#     return dp[m][n]
# s1 = 'abcedefeas'
# s2 = 'abxdefeaef'
# print(minDistance(s1,s2))
#
# def LPS(s):
#     n = len(s)
#     dp = [[0 for i in range(n)]for j in range(n)]
#     for i in range(n):
#         dp[i][i] = 1
#     for i in range(n-1,-1,-1):
#         for j in range(i+1,n):
#             if s[i] == s[j]:
#                 dp[i][j] = dp[i+1][j-1] + 2
#             else:
#                 dp[i][j] = max(dp[i+1][j],dp[i][j-1])
#     return dp[0][n-1]
# s = 'aba'
# print(LPS(s))
#
# def rob(nums):
#     n = len(nums)
#     dp = [0 for _ in range(n+2)]
#     for i in range(n-1,-1,-1):
#         dp[i] = max(dp[i+1],dp[i+2]+nums[i])
#     return dp[0]
# nums = [2,3,5,3,5,7]
# print(rob(nums))

def circleRob(nums):
    n = len(nums)
    if n == 0 : return 0
    if n == 1 : return nums[0]
    return max(rob(0,n-1,nums),rob(1,n,nums))
def rob(start,end,nums):
    n = len(nums)
    dp = [0 for i in range(n+2)]
    for i in range(end-1,start-1,-1):
        dp[i] = max(dp[i+1],dp[i+2]+nums[i])
    return dp[i]
nums = [2,3,5,3,5,7]
print(circleRob(nums))


