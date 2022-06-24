# Python Time Delta - Hackerrank

# Day dd Mon yyyy hh:mm:ss +xxxx

# def time_delta(t1, t2):

#     import datetime

#     time1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
#     time2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

#     return str(abs(int((time1 - time2).total_seconds())))


# print(
#     time_delta("Sat 02 May 2015 19:54:36 +0530",
#                "Fri 01 May 2015 13:54:36 -0000")
# )

# -----------------------------------------------------

# Find-a-word - HackerRank

# def solution(sentences, words):

#     import re

#     for word in words:

#         count = 0

#         for sentence in sentences:

#             match = re.findall(r'\b%s\b' % word, sentence)

#             count += len(match)

#         print(count)


#  ---------------------------------------------------


# apple and oranges - HackerRank

# def countApplesAndOranges(s, t, a, b, apples, oranges):

#     apples_pos = [a + apple for apple in apples if a +
#                   apple >= s and a + apple <= t]
#     oranges_pos = [b + orange for orange in oranges if b +
#                    orange >= s and b + orange <= t]

#     print(len(apples_pos))
#     print(len(oranges_pos))

# -----------------------------------------------------

# Organizing contianers of balls - HackerRank

# def organizingContainers(container):

#     container_totals = []
#     type_totals = []

#     for i in range(len(container)):

#         sum_row = sum(container[i])
#         container_totals.append(sum_row)

#         sum_col = sum([x[i] for x in container])
#         type_totals.append(sum_col)

#     if sorted(container_totals) != sorted(type_totals):
#         return "Impossible"
#     else:
#         return 'Possible'


# print(
#     organizingContainers([[997612619, 934920795, 998879231, 999926463],
#                           [960369681, 997828120, 999792735, 979622676],
#                           [999013654, 998634077, 997988323, 958769423],
#                           [997409523, 999301350, 940952923, 993020546]])
# )

# --------------------------------------------------------

# bigger is greater - HackerRank

# def biggerIsGreater(w):

#     if ''.join(sorted(list(w), reverse=True)) == w:
#         return 'no answer'

#     for i in range(len(w) - 1, -1, -1):

#         if i != len(w) - 1 and w[i] < w[i+1]:
#             s = sorted(w[i+1:])
#             w = list(w[:i+1] + ''.join(s))

#             j = i

#             while j < len(w):
#                 print(w[j] > w[i])
#                 if w[j] > w[i]:
#                     w[j], w[i] = w[i], w[j]
#                     break
#                 j += 1

#             return ''.join(w)


# print(biggerIsGreater('abcd'))

# ----------------------------------------------------------

# Staircase - HackerRank

# def staircase(n):

#     for i in range(1, n+1):
#         print((' ' * (n-i)) + (i * '#'))


# staircase(6)

# ---------------------------------------------------------------------


# String Similarity - HackerRank

# def stringSimilarity(s):

#     total = 0
#     suffix = []

#     for i in range(len(s)):
#         suffix.append(s[i:])

#     for j in suffix:
#         count = 0

#         for idx, val in enumerate(j):
#             if j[idx] == s[idx]:
#                 count += 1
#             else:
#                 break
#         total += count

#     return total


# print(
#     stringSimilarity('ababaa')
# )

# ----------------------------------------------

# Bomber-man - HackerRank


# def bomberMan(n, grid):

#     if n == 1:
#         return grid

#     if n % 2 == 0:
#         return [x.replace('.', 'O') for x in grid]

#     states = [grid]

#     r = len(grid)
#     c = len(grid[0])

#     for state in range(2):
#         tmp = [['O'] * c for _ in range(r)]
#         for i in range(r):
#             for j in range(c):
#                 if states[state][i][j] == 'O':
#                     tmp[i][j] = '.'
#                     if i + 1 < r:
#                         tmp[i+1][j] = '.'
#                     if i - 1 >= 0:
#                         tmp[i-1][j] = '.'
#                     if j + 1 < c:
#                         tmp[i][j+1] = '.'
#                     if j - 1 >= 0:
#                         tmp[i][j-1] = '.'

#         states.append([''.join(s) for s in tmp])

#     if (n-3) % 4 == 0:
#         return states[1]
#     else:
#         return states[2]


# print(
#     bomberMan(2, ['.......',
#               '...O.O.',
#                   '....O..',
#                   '..O....',
#                   'OO...OO',
#                   'OO.O...'])
# )

# -----------------------------------------------

# lily's homework - hackerRank


# def lilysHomework(arr):

#     def solution(arr):

#         hash = {}

#         for num in range(len(arr)):
#             hash[arr[num]] = num

#         nums = arr.copy()
#         s = sorted(nums)

#         count = 0

#         for i in range(len(nums)):
#             if nums[i] != s[i]:
#                 count += 1
#                 idx = hash[s[i]]
#                 nums[i], nums[idx] = nums[idx], nums[i]
#                 hash[nums[idx]] = hash[nums[i]]
#         return count

#     return min(solution(arr), solution(arr[::-1]))


# print(
#     lilysHomework([3, 4, 2, 5, 1])
# )

# --------------------------------------------------------

# Bear and Steady Gene - HackerRank

# def steadyGene(gene):

#     hash_gene = {'A': 0, 'G': 0, 'T': 0, 'C': 0, }
#     hash_pattern = {'A': 0, 'G': 0, 'T': 0, 'C': 0, }
#     n = len(gene)/4

#     for i in gene:
#         hash_pattern[i] += 1

#     for key, value in hash_pattern.items():
#         if value >= n:
#             hash_pattern[key] -= n
#         else:
#             hash_pattern[key] = 0

#     s_len = len(gene)
#     p_len = sum([nums for nums in hash_pattern.values()])

#     if p_len == 0:
#         return 0

#     start, start_index, min_len = 0, -1, s_len

#     count = 0

#     for idx, i in enumerate(gene):

#         hash_gene[i] += 1

#         if hash_gene[i] <= hash_pattern[i]:
#             count += 1

#         if count == p_len:

#             while (hash_gene[gene[start]] > hash_pattern[gene[start]]) or hash_pattern[gene[start]] == 0:

#                 if hash_gene[gene[start]] > hash_pattern[gene[start]]:
#                     hash_gene[gene[start]] -= 1

#                 start += 1

#             len_window = idx - start + 1

#             if min_len > len_window:
#                 min_len = len_window
#                 start_index = start

#     if start_index == -1:
#         return len(gene)

#     return min_len


# print(
#     steadyGene('TATATAGCTTGTCTCCCTAATGTTAGTTCATGCTCGTAAGAGAACTTAGCCTACTAGGACGAGAGAACCGCACGGCGTCGTGAGGTATTTTTCGTAGGACACGCCAGATAGACGGTGGCAATGCCCGTTCAATATGACGCGATGTACGGCTAATGGGAACACTGCCCGACGCGTCTTTAGGACTGTGAGTTGCGGGTTACAGCTATGGTCTTATTGGTATCCGGCCCCTTTCGAGTCGCGATGCGCCTGCCACCACGATATTCGCCCGAAACGCGATTTGTGGGCGAGGTAGTCGTGTTCAACCCTGTAAATTTCCCTAGGTATAATCGTTCTAAGGTTCGCACATACACATCCACACCTACCTTTACACAGTTCGAGGTTCTATACGTCCTCTGAGTGCGTGTTAACACGCCCGTAAATGGGCATTTGGAGTCAGACCAGTACTTTGCGATAAACTTTACTTCCGCGAGACCTGTCCCTGGAACCCTGTTGTAAGGGTTAGGGTTTAATAGCTCCATGTCGTGTGCCTATAAGAAAAGGACGAATGGTGACAGTCCGGCTTAGCCAGGACAATGCGTGGCTGACGACGTCCAGGGTAAATTGAGTTGAATTCGCCTAATTTTAGGGTGTCTTGGTTCAATGAGGTGTCGACTTAACAAAAGGCGACATCAGTTGTCATCTTGCCTTGATAAAGTAAAACACGTGAATAGCCTATCCGGTCTGACCCCCGGGCCATGTGCTTCACCCAGGGAGCATCGCCGCTCTAGAGACGGTGTTCGTAGTCTCGATAACATGTGGGGTAATATAGAATATCCAAGACCGGTAGGAGGGGCGGTTCCGCGTCATAAGAAGTCCCAACGTGGCCTGCCACGTTCAAACAGGATACGCTATAACAGCTTCGTGGGTAATTGATGGATACGCCCGCAGGCTACCCATGCTCTTGCGATTTTGCAACCCTCGGAACCGTCACTCGTACACCCAGACATCATCTCATACAATTGCCTCACCTTCATGCCGGTACATAGGTGCCATCTCCGCTTAAGAATCCTCGCAGCAATTAATGTGACAGCACGCTAGTCCACTAGCGTATGATTACGCCACCGGGCCACCATGGACAAAAACGTTGAATTCCGACTAATAGACGAGTGTCCGATCGGGTCAACCGATCTCGGATGTTGCGTACCAGGACTACTGGGCTCGGGCCGAATCAGACACACGTATGCAACAGATACCGATAGGCGTCTTCCTAAGTAACAGCCGTAATCAATGGTGCCACAGATCTACTAATTACGGTGAAGATCATGGCCCACGACGCTGTACGGGTTTATAGCTGCCACAAACTTTAGGAAGTTTCAGCAATCGACGCGTAGTATGTGTGCTCAGACGGGTCGAGCATGCACTTGTGTATTAAGTTACTTGGCTGAACAACCTGTTGATAGATCTTGAGAGGACCGAGAAATTGCCCTCCGGTTATGAAACAGGTCCTGCGTACCAATCCTT')
# )


# ---------------------------------------------------------

# Minimum Loss - HackerRank

# def minimumLoss(price):

#     minLoss = float('inf')

#     projected = sorted(price, reverse=True)

#     for i in range(len(projected)-1):

#         if (projected[i] - projected[i + 1]) < minLoss:
#             if price.index(projected[i]) < price.index(projected[i + 1]):
#                 minLoss = projected[i] - projected[i+1]

#     return minLoss


# print(
#     minimumLoss([5, 10, 3])
# )


# --------------------------------------------------------


# Journey to the Moon - HackerRank

# def jouneryToMoon(n, astronaut):

#     from collections import defaultdict

#     p = list(range(n))

#     def find(x):
#         if x != p[x]:
#             p[x] = find(p[x])
#         return p[x]

#     def union(x, y):
#         px = find(x)
#         py = find(y)

#         if px != py:
#             p[py] = px

#     for x, y in astronaut:
#         union(x, y)

#     mydict = defaultdict(list)
#     for i, val in enumerate(p):
#         mydict[find(val)].append(i)

#     groups = [len(x) for x in mydict.values() if len(x) > 1]
#     groups.append(n-sum(groups))

#     res = 0

#     a = groups[len(groups) - 1]

#     for j in range(len(groups)-1):
#         res += groups[j] * sum(groups[j + 1:])

#     return res + int((a * (a - 1))/2)


# print(
#     jouneryToMoon(100000, [[1, 2], [3, 4]])
# )


# bfsshortestreach - leetcode

# def bfs(n, m, edges, s):

#     nodes = {}
#     p = [-1 for x in range(n+1)]

#     for i in edges:

#         if i[0] in nodes:
#             if i[1] not in nodes[i[0]]:
#                 nodes[i[0]].append(i[1])
#         else:
#             nodes[i[0]] = [i[1]]

#         if i[1] in nodes:
#             if i[0] not in nodes[i[1]]:
#                 nodes[i[1]].append(i[0])
#         else:
#             nodes[i[1]] = [i[0]]

#     nodes_to_traverse = [s]
#     count = 0

#     while nodes_to_traverse:

#         next = []

#         for i in nodes_to_traverse:
#             p[i] = count*6
#             for k in nodes[i]:
#                 if p[k] == -1:
#                     next.append(k)
#         nodes_to_traverse = next
#         count += 1

#     p.remove(0)

#     return p[1:]


# print(
#     bfs(9, 5, [[3, 4], [3, 6], [3, 2], [9, 4], [8, 4], ], 3)
# )
# print(
#     bfs(3, 1, [[2, 3]], 2)
# )

# --------------------------------------------------------

# def r(text):

#     import re

#     match = re.findall(
#         r'((?<=href=").+?(?="))(?:.+?)((?:><\/a>)|(?<=>(?!<)).*?(?=<\/a>))', text)

#     for t in match:
#         if t[1] == '></a>':
#             print(t[0])
#         else:
#             print(','.join(t))


# s = """<li class="interwiki-ar"><a href="//ar.wikipedia.org/wiki/" title="" lang="ar" hreflang="ar"></a></li>"""

# r(s)

# ---------------------------------------------------------------

# def numCells(grid):
#     # Write your code here

#     adj = [(-1, 0), (-1, 1), (0, 1), (1, 1),
#            (1, 0), (1, -1), (0, -1), (-1, -1)]

#     count = 0

#     for i in range(len(grid)):
#         for j in range(len(grid[i])):

#             adj_nums = []

#             for x, y in adj:
#                 print(i+x, j + y)
#                 if (i + x) >= 0 and (i + x) < len(grid) and (j + y) >= 0 and (j + y) < len(grid[i]):
#                     adj_nums.append(grid[i+x][j+y])

#             if all(k < grid[i][j] for k in adj_nums):
#                 count += 1

#     return count


# numCells([[1, 2, 2, 1]])


# ----------------------------------------------------------------

# 148. Sort List - Leetcode

# def sortList(head):

#     nodes = []

#     n = head
#     while n:
#         nodes.append(n)
#         n = n.next

#     nodes.sort(key=lambda node: node.val)

#     s = None
#     for i in range(len(nodes)-1, -1, -1):
#         nodes[i].next = s
#         s = nodes[i]

#     return nodes

# ---------------------------------------------------------------

# 162. Find Peak Element - leetcode

# def findPeakElement(nums):

#     if len(nums) <= 1:
#         return 0

#     for i in range(len(nums) - 1):
#         if nums[i] > nums[i+1]:
#             return i

#     return len(nums) - 1

# ----------------------------------------------------------------

# 4. Median of Two Sorted Arrays - leetcode

# def findMedianSortedArray(nums1, nums2):

#     A, B = nums1, nums2
#     total = len(nums1) + len(nums2)

#     target = total//2

#     # Get lowest smallest array
#     if len(A) > len(B):
#         A, B = B, A

#     l, r = 0, len(A) - 1

#     while True:

#         i = (l+r)//2  # A
#         j = target - i - 2  # B

#         A_left = A[i] if i >= 0 else float('-inf')
#         A_right = A[i+1] if i + 1 < len(A) else float('inf')
#         B_left = B[j] if j >= 0 else float('-inf')
#         B_right = B[j+1] if j + 1 < len(B) else float('inf')

#         # Check condition
#         if A_left <= B_right and B_left <= A_right:
#             # Odd
#             if total % 2 != 0:
#                 return min(A_right, B_right)
#             else:
#                 # Even
#                 return (max(A_left, B_left) + min(A_right, B_right)) / 2
#         elif A_left > B_right:
#             r = i - 1
#         else:
#             l = i + 1


# print(
#     findMedianSortedArray([2], [1, 2, 3])
# )


# --------------------------------------------------------------------

# 1642. Furthest Building You Can Reach - leetcode

# def furthestBuilding(heights, bricks, ladders):

#     b, l = bricks, ladders

#     diff_heights = []

#     i = 0
#     while True:
#         if i == (len(heights) - 1):
#             return i

#         diff = heights[i+1] - heights[i]

#         if diff > 0:
#             b -= diff
#             diff_heights.append(diff)
#         else:
#             diff_heights.append(0)

#         while b <= 0 and l > 0:
#             m = max(diff_heights)
#             b += m
#             diff_heights.remove(m)
#             l -= 1

#         if b <= 0 and l <= 0 and diff > 0:
#             return i

#         i += 1


# print(
#     furthestBuilding([11, 10, 20, 30], 0, 0)
# )

# --------------------------------------------------------


# 1642. Furthest Building You Can Reach - leetcode


def furthestBuilding(heights, bricks, ladders):
    import heapq

    b, l = bricks, ladders
    n = len(heights)

    diff_heights = []

    for i in range(n - 1):

        diff = heights[i+1] - heights[i]

        if diff > 0:
            b -= diff
            heapq.heappush(diff_heights, -diff)

        while b < 0 and l > 0:
            m = heapq.heappop(diff_heights)
            b += -m
            l -= 1

        if b < 0 and l <= 0 and diff > 0:
            return i

    return n - 1


print(
    furthestBuilding(

        [1, 2, 4, 7], 3, 1)
)
