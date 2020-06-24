from collections import Counter
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
            if valid == len(t):
                res.append(left)
            d = s[left]
            left += 1
            if need.__contains__(d):
                if need[d] == window[d]:
                    valid -= 1
                    window[d] -= 1
    return res
s = 'cbaebabacd'
t = 'abc'
print(findAnagram(s,t))

