def binarySearch(nums,target):
    left = 0
    right = len(nums) - 1
    while(left < right):
        mid = int((left+right)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1
nums = [1,2,3,5,6]
target = 5
print(binarySearch(nums,target))

def twoSum(nums,target):
    left = 0
    right = len(nums) - 1
    while(left < right):
        sum = nums[left] + nums[right]
        if sum == target:
            return left+1,right+1
        elif sum > target:
            right -= 1
        elif sum < target:
            left += 1
    return -1,-1
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))

def reverse(nums):
    left = 0
    right = len(nums)-1
    while(left<right):
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
    return nums
nums = [12,3,4,7,8]
print(reverse(nums))

from collections import Counter
def minWindow(s,t):
    window = Counter()
    need = Counter(t)
    left,right = 0,0
    valid = 0
    minLen = float('inf')

    while(right<len(s)):
        c = s[right]
        right += 1
        if need.__contains__(c):
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        while valid == len(t):
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
s = "ABEIFYRCABC"
t = "ABC"
print(minWindow(s,t))