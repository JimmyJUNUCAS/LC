# Q1 打家劫舍
# def rob(nums):
#     n = len(nums)
#     dp = [0 for _ in range(n+2)]
#     for i in range(n-1,-1,-1):
#         dp[i] = max(dp[i+1],dp[i+2]+nums[i])
#     return dp[0]
#
# nums = [2,3,5,3,5,7]
# print(rob(nums))
# Q2

# def circleRob(nums):
#     n = len(nums)
#     if n == 0 : return 0
#     if n == 1 : return nums[0]
#     return max(rob(nums,0,n-2),rob(nums,1,n-1))
# def rob(nums,start,end):
#     n = len(nums)
#     dp = [0 for _ in range(n+1)]
#     for i in range(end-1,start-1,-1):
#         dp[i] = max(dp[i+1],dp[i+2]+nums[i])
#     return dp[i]
# nums = [2,3,5,3,5,7]
# print(circleRob(nums))

# Q3
# def longestCommonSubsequence(str1,str2):
#     m,n = len(str1),len(str2)
#     dp = [[0 for _ in range(n+1)]for i in range(m+1)]
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if str1[i-1] == str2[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
#     return dp[-1][-1]
#
#
# str1 = 'abc'
# str2 = 'eiwdlatbldc'
# print(longestCommonSubsequence(str1,str2))

# Q4
# def lengthofLIS(nums):
#     n = len(nums)
#     dp = [1 for _ in range(n)]
#     for i in range(n):
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 dp[i] = max(dp[i],dp[j]+1)
#     return max(dp)
#
# num = [1,6,2,7,2,6,1,9]
# print(lengthofLIS(num))

# Q5
# def minDistance(s1,s2):
#     def dp(i,j):
#         if i == -1: return j + 1
#         if j == -1: return i + 1
#         if s1[i] == s2[j]:
#             return dp(i-1,j-1)
#         else:
#             return min(dp(i-1,j)+1,dp(i,j-1)+1,dp(i-1,j-1)+1)
#     return dp(len(s1)-1,len(s2)-1)
#
# s1 = 'abcedefeas'
# s2 = 'abxdefeaef'
# print(minDistance(s1,s2))

