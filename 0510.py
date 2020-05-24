# def maxA(N):
#     dp = [0 for _ in range(N+1)]
#     for i in range(1,N+1):
#         dp[i] = dp[i-1] + 1
#         for j in range(2,i):
#             dp[i] = max(dp[i],dp[j-2]*(i-j+1))
#     return dp[N]
#
# N = 9
# print(maxA(N))

# def maxA(N):
#     dp = [0 for _ in range(N+1)]
#     for i in range(1,N+1):
#         dp[i] = dp[i-1] + 1
#         for j in range(2,i):
#             dp[i] = max(dp[i],dp[j-2]*(i-j+1))
#     return dp[N]
# N = 9
# print(maxA(N))

# def StoneGame(piles):
#     n = len(piles)
#     dp = [[[0 for _ in range(2)]for i in range(n)]for j in range(n)]
#     for i in range(n):
#         dp[i][i][0] = piles[i]
#         dp[i][i][1] =  0
#     for l in range(1,n):
#         for i in range(n-l):
#             j = l + i
#             left = piles[i] + dp[i+1][j][1]
#             right = piles[j] + dp[i][j-1][1]
#             if(left > right):
#                 dp[i][j][0] = left
#                 dp[i][j][1] = dp[i+1][j][0]
#             else:
#                 dp[i][j][0] = right
#                 dp[i][j][1] = dp[i][j-1][0]
#     return dp[0][n-1][0] - dp[0][n-1][1]

# def stoneGame(piles):
#     n = len(piles)
#     dp = [[[0 for _ in range(2)]for i in range(n)]for j in range(n)]
#     for i in range(n):
#         dp[i][i][0] = piles[i]
#         dp[i][i][1] = 0
#     for l in range(1,n):
#         for i in range(n-l):
#             j = i + l
#             left = piles[i] + dp[i+1][j][1]
#             right = piles[j] + dp[i][j-1][1]
#             if(left>right):
#                 dp[i][j][0] = left
#                 dp[i][j][1] = dp[i+1][j][0]
#             else:
#                 dp[i][j][0] = right
#                 dp[i][j][1] = dp[i][j-1][0]
#     return dp[0][n-1][0]-dp[0][n-1][1]
#
# piles = [10,3,4]
# print(stoneGame(piles))

# def LIS(piles):
#     n = len(piles)
#     dp = [1 for _ in range(n)] #init as 1 not 0
#     for i in range(n):
#         for j in range(i):
#             if piles[i] > piles[j]:
#                 dp[i] = max(dp[i],dp[j]+1)
#     return max(dp)
#
# piles = [1,3,4,5,3,6,2,5]
# print(LIS(piles))
# def LIS(nums):
#     n = len(nums)
#     dp = [1 for i in range(n)]
#     for i in range(n):
#         for j in range(i):
#             if(nums[i] > nums[j]):
#                 dp[i] = max(dp[i],dp[j]+1)
#     return max(dp)
# piles = [1,3,4,5,3,6,2,5]
# print(LIS(piles))

# 遍历的方向：正序，逆序，斜着
# 遍历的原则：遍历过程所需要的状态已经计算出来了
#            遍历终点是存储结果那个位置
# def rob(nums):
#     n = len(nums)
#     dp = [0 for i in range(n+2)]
#     for i in range(2,n+2):
#         dp[i] = max(dp[i-1],dp[i-2]+nums[i-2])
#     return dp[n+1]
#
# nums = [2,3,5,3,5,7]
# print(rob(nums))

# def rob(nums):
#     n = len(nums)
#     dp = [0 for i in range(n+2)]
#     for i in range(n-1,-1,-1):
#         dp[i] = max(dp[i+1],dp[i+2]+nums[i])
#     return dp[0]
# nums = [2,3,5,3,5,7]
# print)(rob(nums)
# # Q1 打家劫舍
# def rob(nums):
#     n = len(nums)
#     dp = [0 for _ in range(n+2)]
#     for i in range(n-1,-1,-1):
#         dp[i] = max(dp[i+1],dp[i+2]+nums[i])
#     return dp[0]
#
# nums = [2,3,5,3,5,7]
# print(rob(nums))

# def rob(nums):
#     n = len(nums)
#     dp = [0 for _ in range(n+2)]
#     for i in range(n-1,-1,-1):
#         dp[i] = max(dp[i+1],dp[i+2]+nums[i])
#     return dp[0]
# nums = [2,3,5,3,5,7]
# print(rob(nums))

# def circleRob(nums):
#     n = len(nums)
#     if n == 0 : return 0
#     if n == 1 : return nums[0]
#     return max(rob(0,n-2,nums),rob(1,n-1,nums))
#
# def rob(start,end,nums):
#     n = len(nums)
#     dp = [0 for _ in range(n+2)]
#     for i in range(end,start-1,-1):
#         dp[i] = max(dp[i+1],dp[i+2]+nums[i])
#     return dp[i]
# nums = [2,3,5,3,5,7]
# print(circleRob(nums))

def circleRob(nums):
    n = len(nums)
    if n == 0 : return 0
    if n == 1 : return nums[0]
    return max(rob(0,n-1,nums),rob(1,n,nums))

def rob(start,end,nums):
    n = len(nums)
    dp = [0 for _ in range(n+2)]
    for i in range(end-1,start-1,-1):
        dp[i] = max(dp[i+1],dp[i+2]+nums[i])
    return dp[i]
nums = [2,3,5,3,5,7]
print(circleRob(nums))
# def circleRob(nums):
#     n = len(nums)
#     if n == 0 : return 0
#     if n == 1 : return nums[0]
#     return max(rob(0,n-2,nums),rob(1,n-1,nums))
#     #记住应该是在数组中的位置值，而不是实际值
#
# def rob(start,end,nums):
#     n = len(nums)
#     dp = [0 for _ in range(n+2)]
#     for i in range(end,start-1,-1):
#         dp[i] = max(dp[i+1],dp[i+2]+nums[i])
#     return dp[i]
# nums = [2,3,5,3,5,7]
# print(circleRob(nums))

# def rob(nums):
#     n = len(nums)
#     dp = [0 for _ in range(n+2)]
#     for i in range(n-1,-1,-1):
#         dp[i] = max(dp[i+1],dp[i+2]+nums[i])
#     return dp[0]
# nums = [2,3,5,3,5,7]
# print(rob(nums))
# 其中边界的范围，要考虑是当前值还是指针值，例如nums的长度为n，但它能取到的最大值是n-1

# dp数组遍历
# 正着遍历
# m = n = 1
# dp = [[0 for _ in range(m)]for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         dp[i][j]
# for i in range(n-1,-1,-1):
#     for j in range(m-1,-1,-1):
#         dp[i][j]
#
# for l in range(n):
#     for i in range(n-l):
#         j = i + l
#         dp[i][j]
#

# def LCS(str1,str2):
#     m,n = len(str1),len(str2)
#     dp = [[0 for i in range(n+1)]for j in range(m+1)]
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if str1[i-1] == str2[j-1]:
#                  dp[i][j] = dp[i-1][j-1] + 1 #代码里面存在i-1，需要将其考虑进去;考虑指针位置
#             else:
#                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
#
#     return dp[m][n]
# str1 = 'abc'
# str2 = 'eiwdlatbldc'
# print(LCS(str1,str2))

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

# def minDistance(str1,str2):
#     m,n = len(str1),len(str2)
#     dp = [[0 for i in range(n+1)]for j in range(m+1)]
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if str1[i-1] == str2[j-1]:
#                 dp[i][j] = dp[i-1][j-1]
#             else:
#                 dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
#     return dp[m][n]
#
# s1 = 'abcedefeas'
# s2 = 'abxdefeaef'
# print(minDistance(s1,s2))

def minDistance(str1,str2):
    m,n = len(str1),len(str2)
    dp = [[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
    return dp[m][n]
s1 = 'abcedefeas'
s2 = 'abxdefeaef'
print(minDistance(s1,s2))

# def superEgg(K,N):
#     memo = dict()
#     def dp(K,N):
#         if N == 0 : return 0
#         if K == 1 : return N
#         if (K,N) in memo:
#             return memo[(K,N)]
#
#         res = float('INF')
#         for i in range(1,N+1):
#             res = min(res,max(dp(K,N-i),dp(K-1,i-1))+1)
#         memo[(K,N)] = res
#         return res
#     return dp(K,N)
# print(superEgg(3,20))

# def superEgg(K,N):
#     memo = dict()
#     def dp(K,N):
#         if N == 0 : return 0
#         if K == 1 : return N
#         if(K,N) in memo:
#             return memo[(K,N)]
#
#         res = float('INF')
#         for i in range(1,N+1):
#             res = min(res,max(dp(K,N-i),dp(K-1,i-1))+1)
#         memo[(K,N)] = res
#         return res
#     return dp(K,N)
# print(superEgg(3,20))

# def superEgg(K,N):
#     if N == 0 : return 0
#     if K == 1 : return N
#     dp = [[0 for i in range(N)]for j in range(K)]
#
#     for i in range(N):
#         dp[K][i] = min(dp[K][i],max(dp[K][N-i],dp[K-1][i-1])+1)
#     return dp[0]





# def superEggDrop(K,N):
#     memo = dict()
#     def dp(K,N):
#         if K == 1: return N
#         if N == 0: return 0
#
#         if (K,N) in memo :
#             return memo[(K,N)]
#
#         res = float('INF')
#         for i in range(1,N+1):
#             res = min(res,max(dp(K,N-i),dp(K-1,i-1))+1)
#         memo[(K,N)] = res
#         return res
#     return dp(K,N)
#
#
# print(superEggDrop(3,20))


