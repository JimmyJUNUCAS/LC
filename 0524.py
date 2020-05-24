# def binarySearch(nums,target):
#     left = 0
#     right = len(nums)-1
#     while left < right:
#         mid = int(left + (right-left)/2)
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             right = mid - 1
#         elif nums[mid] < target:
#             left = mid + 1
#     return -1
# nums = [1,2,3,5,6]
# target = 1
# print(binarySearch(nums,target))
#
# def twoSum(nums,target):
#     left = 0
#     right = len(nums)-1
#     while left < right:
#         sum = nums[left] + nums[right]
#         if sum == target:
#             return left + 1,right + 1
#         elif sum > target:
#             right -= 1
#         elif sum < target:
#             left += 1
#     return -1,-1
# nums = [2,7,11,15]
# target = 13
# print(twoSum(nums,target))
#
# def reverse(nums):
#     left = 0
#     right = len(nums)-1
#     while left < right:
#         temp = nums[left]
#         nums[left] = nums[right]
#         nums[right] = temp
#         left += 1
#         right -= 1
#     return nums
# nums = [12,3,4,7,8]
# print(reverse(nums))

from collections import Counter
def minWindow(s,t):
    window = Counter()
    need = Counter(t)
    left,right = 0,0
    valid = 0
    minLen = float('inf')

    while right < len(s):
        c = s[right]
        right += 1
        if need.__contains__(c):
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        while valid >= len(t):
            if right - left < minLen:
                start = left
                minLen = right - left
            d = s[left]
            left += 1
            if need.__contains__(d):
                if window[d] == need[d]:
                    valid -= 1
                    window[d] -= 1
    if minLen == float('inf'):
        return ""
    else:
        return start,minLen

s = 'ABSKWIFIECABC'
t = 'ABC'
print(minWindow(s,t))

def findAnagram(s,t):
    window = Counter()
    need = Counter(t)
    left,right = 0,0
    valid = 0
    res = []

    while right < len(s):
        c = s[right]
        right += 1
        if need.__contains__(c):
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        while right - left >= len(t):
            if valid == len(need):
                res.append(left)
            d = s[left]
            left += 1
            if need.__contains__(d):
                if window[d] == need[d]:
                    valid -= 1
                    window[d] -= 1
    return res
s = 'cbaebabacd'
t = 'abc'
print(findAnagram(s,t))

def checkInClusion(s,t):
    window = Counter()
    need = Counter(t)
    left,right = 0,0
    valid = 0

    while right < len(s):
        c = s[right]
        right += 1
        if need.__contains__(c):
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        if right - left >= len(t):
            if valid == len(need):
                return True
            d = s[left]
            left += 1
            if need.__contains__(d):
                if window[d] == need(d):
                    valid -= 1
                    window[d] -= 1
    return False
s1 = 'ab'
s2 = 'eidbaoooo'
print(checkInClusion(s2,s1))

def LengthOfLongestSubString(s):
    window = Counter()
    left,right = 0,0
    res = 0
    while right < len(s):
        c = s[right]
        right += 1
        window[c] += 1
        while window[c] > 1:
            d = s[left]
            left += 1
            window[d] -= 1
        res = max(res,right-left)
    return res
s = 'abcabcbb'
print(LengthOfLongestSubString(s))


def minWindow(s,t):
    window  = Counter()
    need = Counter(t)
    left,right = 0, 0
    valid = 0
    minLen = float('inf')

    while right < len(s):
        c = s[right]
        right += 1
        if need.__contains__(c):
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        while valid >= len(t):
            if right - left < minLen:
                start = left
                minLen = right - left
            d = s[left]
            left += 1
            