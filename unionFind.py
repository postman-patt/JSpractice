
# 1202. Smallest String With Swaps

# def smallestStringWithSwaps(s, pairs):


#     hash = {}

#     for i in pairs:

#         s1 = i[0]
#         s2 = i[1]
        
#         if s1 not in hash and s2 not in hash:
#             hash[s1], hash[s2] = [s[s1], s[s2]]
            
#         if s1 in hash and s2 in hash:
#             n = hash[s1] + hash[s2]

#         else:


# ------------------------------------------------------------------

# Union Find

def smallestStringWithSwaps(s, pairs):

    p = list(range(len(s)))

    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]

    def union(x, y):
        px = find(x)
        py = find(y)

        if px != py:
            p[py] = px

    for x, y in pairs:
        union(x, y)

    print(p)

    hash = defaultdict(list)
    for i, val in enumerate(p):
        hash[find(val)].append(i)

    res = list(s)

    print(hash)

    for x in hash.keys():
        chars = [s[k] for k in hash[x]]
        chars.sort()

        for idx, char in zip(hash[x], chars):
            res[idx] = char

    
    return ''.join(res)

    
        
print(
smallestStringWithSwaps('bcad', [[0,3],[1,2],[0,2]])
)
        