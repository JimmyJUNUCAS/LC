from collections import Counter
def minWindow(s,t):
    window = Counter()
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

def checkInclusion(s,t):
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
        while right - left >= len(t):
            if valid == len(need):
                return True
            d = s[left]
            left += 1
            if need.__contains__(d):
                if window[d] == need[d]:
                    valid -= 1
                    window[d] -= 1
    return False
s1 = 'ab'
s2 = 'eidboaoooo'
print(checkInclusion(s2,s1))

def lengthOfLongestSubString(s):
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
print(lengthOfLongestSubString(s))