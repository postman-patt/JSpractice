

# Journey to the Moon - HackerRank

def jouneryToMoon(n, astronaut):

    from collections import defaultdict

    p = list(range(n))

    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]

    def union(x, y):
        px = find(x)
        py = find(y)

        if px != py:
            p[py] = px

    for x, y in astronaut:
        union(x, y)

    mydict = defaultdict(list)
    for i, val in enumerate(p):
        mydict[find(val)].append(i)

    groups = [len(x) for x in mydict.values() if len(x) > 1]
    groups.append(n-sum(groups))

    res = 0

    a = groups[len(groups) - 1]

    for j in range(len(groups)-1):
        res += groups[j] * sum(groups[j + 1:])

    return res + int((a * (a - 1))/2)


print(
    jouneryToMoon(100000, [[1, 2], [3, 4]])


)
