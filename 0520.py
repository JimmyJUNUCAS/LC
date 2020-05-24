from collections import Counter
def minWindow(s,t):
    window = Counter()
    need = Counter(t)
    left,right = 0,0
    valid = 0
    minLen = float('inf')

    while(right < len(s)):
        c = s[right]
        right += 1
        if need .__contains__(c):
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        while(valid == len(need)):
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
        return " "
    else:
        return start,minLen


s = 'ABSKWIFIECABC'
t = 'ABC'
print(minWindow(s,t))