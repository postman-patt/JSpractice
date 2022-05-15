# String Similarity - HackerRank

def solution(s):
    
    z = [0 for x in range(len(s))]
    left = 0
    right = 0

    for k in range(len(s)):
        if k > right:
            left = right = k
            while(right < len(s) and s[right] == s[right - left]):
                right += 1
            z[k] = right - left
            right -= 1
        else:
            k1 = k - left
            if z[k1] < right - k +1:
                z[k] = z[k1]
            else:
                left = k
                while right < len(s) and s[right] == s[right -left]:
                    right += 1
                z[k] = right - left
                right -= 1

    return sum(z) + len(s)

print(
solution('ababaa'))