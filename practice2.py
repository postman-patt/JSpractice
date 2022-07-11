# HackerRank - The Minion Game

# def minion_game(string):

#     newstr = ''.join(string.split())

#     string_permutations = [newstr[i:j] for i in range(len(newstr)) for j in range(i+1, len(newstr) +1)]

#     countA = 0
#     countB = 0

#     print(set(string_permutations))

#     for x in set(string_permutations):

#         if x[0] in "AEIOU":
#             countB += string_permutations.count(x)

#         if x[0] in "BCDFGHJKLMNPQRSTVWXYZ":
#             countA += string_permutations.count(x)

#     if countA > countB:
#         print("Stuart %d" % countA)
#     elif countA < countB:
#         print("Kevin %d" % countB)
#     else:
#         print('Draw')


# minion_game("COOLIOBROSKIIUEWHFIEFIEHFDEWHIODFEHFIHWEFOWEHOFHWEOFHEWOHFEWOLHFDLOEWHDFWENIEWEWF")

# ----------------------------------------------------------------

# def minion_game(string):

#     s = 0
#     k = 0

#     for i, val in enumerate(string):

#         if val in "AEIOU":
#             k += len(string) - i
#         else:
#             s += len(string) - i

#     if s> k:
#         print("Stuart %d" % s)
#     elif s< k:
#         print("Kevin %d" % k)
#     else:
#         print("Draw")

# minion_game('BANANA')

# ----------------------------------------------------------------

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string) - len(sub_string)+1):
#         if string[i: i+ len(sub_string)].find(sub_string) != -1 :
#             count += 1
#     return count

# print(
# count_substring("ABCDCDC", "CDC"))

# ------------------------------------------------------------------

# # Piling Up - HackerRank
# def solution(blocks, n):

#     left = 0
#     right = len(blocks) - 1

#     num = max(blocks[left], blocks[right])

#     while left <= right:

#         if blocks[left] <= num and blocks[right] <= num:
#             if blocks[left] >= blocks[right]:
#                 num = blocks[left]
#                 left += 1
#             else:
#                 num = blocks[right]
#                 right -= 1
#         elif blocks[left] <= num:
#             num = blocks[left]
#             left += 1
#         elif blocks[right] <= num:
#             num = blocks[right]
#             right -= 1
#         else:
#             return("No")

#     return("Yes")

# def main():
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         blocks = list(map(int, input().strip().split()))
#         print(solution(blocks, n))

# if __name__ == '__main__':
#     main()

# -------------------------------------------------------------------------

# No-idea - HackerRank

# def solution(nums, setA, setB):

#     hashA = {}
#     hashB = {}

#     for x in setA:
#         if x not in hashA:
#             hashA[str(x)] = True

#     for k in setB:
#         if k not in hashB:
#             hashB[str(k)] = True

#     count = 0

#     for i in nums:

#         if str(i) in hashA:
#             count += 1

#         if str(i) in hashB:
#             count -= 1

#     return count

# def main():
#     n = input()
#     m = input()
#     nums = list(map(int, input().strip().split()))
#     setA = list(map(int, input().strip().split()))
#     setB = list(map(int, input().strip().split()))
#     print(nums, setA, setB)
#     print(solution(nums, setA, setB))

# print(
# solution([1, 2, 3, 4, 5], [2, 3], [4])
# )

# ---------------------------------------------------------------------------


# Word order - HackerRank

# def solution(words):

#     hash = {}

#     for i in words:

#         if i not in hash:
#             hash[i] = 1
#         else:
#             hash[i] += 1

#     return str(len(set(hash.keys()))) + "\n" + ' '.join([str(k) for k in hash.values()])


# if __name__ == '__main__':

#     words = [input() for i in range(int(input()))]

# print(
# solution(['bcdef', 'abcdefg', 'bcde', 'bcdef']))

# -----------------------------------------------------------------------

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

# def smallestStringWithSwaps(s, pairs):

#     p = list(range(len(s)))

#     def find(x):
#         if x != p[x]:
#             p[x] = find(p[x])
#         return p[x]

#     def union(x, y):
#         px = find(x)
#         py = find(y)

#         if px != py:
#             p[py] = px

#     for x, y in pairs:
#         union(x, y)

#     print(p)

#     hash = defaultdict(list)
#     for i, val in enumerate(p):
#         hash[find(val)].append(i)

#     res = list(s)

#     print(hash)

#     for x in hash.keys():
#         chars = [s[k] for k in hash[x]]
#         chars.sort()

#         for idx, char in zip(hash[x], chars):
#             res[idx] = char


#     return ''.join(res)


# print(
# smallestStringWithSwaps('bcad', [[0,3],[1,2],[0,2]])
# )

# ---------------------------------------------------------------------

# 844. Backspace String Compare - leetcode

# def backspaceCompare(s, t):

#     stack_s = []
#     stack_t = []

#     for char_s in s:

#         if char_s != "#":
#             stack_s.append(char_s)
#         else:
#             if len(stack_s) > 0:
#                 stack_s.pop()

#     for char_t in t:
#         if char_t != "#":
#             stack_t.append(char_t)
#         else:
#             if len(stack_t) > 0:
#                 stack_t.pop()

#     print(stack_t, stack_s)

#     if stack_s == stack_t:
#         return True
#     else:
#         return False

# print(backspaceCompare(
# "xywrrmp",
# "xywrrmu#p"))

# -------------------------------------------------------------------

# Most Commons - HackerRank

# def mostCommon(s):

#     dict = {}

#     for i in sorted(s):

#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1

#     sorted_dict = sorted([key for key in dict], key = lambda k: dict[k], reverse=True)[:3]

#     for key in sorted_dict:
#         print(key + ' ' + str(dict[key]))


# mostCommon("GOOGLE")


# -----------------------------------------------------------------

# Merge the Tools - Hackerank

# def merge_the_tools(string, k):

#     substr = [ [x for x in string[i*k:i*k+k]] for i in range(int(len(string)/k))]

#     for j in substr:
#         hash = {}
#         for n in j:
#             if n not in hash:
#                 hash[n] = 1
#         print(''.join([l for l in hash]))


# merge_the_tools('AAABCADDE', 3)

# ---------------------------------------------------------------

# List Comprehension - HackerRank

# def solution(i, j, k, n):

#     return sorted([[x, y, z] for z in range(k+1) for y in range(j+1) for x in range(i+1) if sum([x, y, z]) != n])

# print(solution(1, 1, 2, 3))

# ---------------------------------------------------------------


# ginortS - HackerRank

# def solution(s):

#     lowercase = ''
#     uppercase = ''
#     odd = ''
#     even = ''

#     for i in s:

#         if i.isupper():
#             uppercase += i

#         if i.islower():
#             lowercase += i

#         if i.isnumeric():
#            if int(i) % 2 == 0:
#                even += str(i)
#            else:
#                odd += str(i)

#     print(''.join(sorted(lowercase) + sorted(uppercase) + sorted(odd) + sorted(even)))

# solution("Sorting1234")

# ---------------------------------------------------------------------------

# Find a Word - HackerRank

# import re

# def solution(s, w):
#     print(len(re.findall('(?:^|\W)(%s)(?:\W|$)' % w, s)))

# if __name__ == "__main__":
#     sentences = [str(input()) for i in range(int(input()))]
#     words = [str(input())for j in range(int(input()))]

#     for word in words:
#         for sentence in sentences:
#             solution(sentence, word)


# ---------------------------------------------------------------------------


# import itertools as iter

# def solution(s):

#     res = []

#     for k, v in iter.groupby(s):
#         res.append('(%s, %s)' % (k, len(list(v))))

#     print(' '.join(res))

# solution('111223345557')

# -------------------------------------------------------------------------


# def solution(h, m):

#     times = {1: 'one',2: 'two',3: 'three',4: 'four',5: 'five',6: 'six',7: 'seven',8: 'eight',9: 'nine', 10: 'ten',11: 'eleven', 12: 'twelve',13: 'thirteen',14: 'fourteen',15: 'quarter',16: 'sixteen',17: 'seventeen',18: 'eighteen',19: 'nineteen', 20:'twenty', 21: 'twenty one', 22: 'twenty two',23: 'twenty three',24: 'twenty four',25: 'twenty five',26: 'twenty six',27: 'twenty seven',28: 'twenty eight',29: 'twenty nine', 30:'half'}

#     if m == '00':
#         return str(times[h]) + " o' clock"

#     minutes = ' minutes'
#     if m == 15 or 60-m == 15:
#         minutes = ''

#     if m <= 30:
#         return times[m] + minutes + " past " + times[h]
#     else:
#         return times[60-m] + minutes + " to " + times[h+1]


# print(solution(5, 45))

# ----------------------------------------------------------

# # Climbing the leaderboard - HackerRank

# def climbingLeaderboard(ranked, player):

#     rank = sorted(list(set(ranked)))
#     res = []

#     for idx, val in enumerate(rank):

#         print(player)

#         while len(player) > 0 and val == player[0]:
#             res.append(len(rank) - idx)
#             player.pop(0)

#         while len(player) > 0 and val > player[0]:
#             res.append(len(rank)-idx +1)
#             player.pop(0)

#     while len(player) > 0:
#         res.append(1)
#         player.pop(0)

#     return res

# print(
# climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))

# -------------------------------------------------------------------------------


# The grid search - HackerRank

# def gridSearch(G, P):

#     for idx_G, line in enumerate(G):

#         indexes = []
#         pointer = 0

#         while line.find(P[0], pointer) != -1:
#             indexes.append(line.find(P[0], pointer))
#             pointer = line.find(P[0], pointer) +1
#         print(indexes)
#         for i in indexes:
#             for idx_P, p in enumerate(P):
#                 if G[idx_G + idx_P][i:i+len(p)] != p:
#                     break
#                 if idx_P == len(P)-1:
#                     return "YES"
#     return "NO"

# print(
# gridSearch(
# ['400453592126560',
# '114213133098692',
# '474386082879648',
# '522356951189169',
# '887109450487496',
# '252802633388782',
# '502771484966748',
# '075975207693780',
# '511799789562806',
# '404007454272504',
# '549043809916080',
# '962410809534811',
# '445893523733475',
# '768705303214174',
# '650629270887160'], ['99', '99']))

# ------------------------------------------------------------------------

# Number Line Jumps - HackerRank

# def numberLineJumps(x1, v1, x2, v2):

#     if v1==v2 and x1 != x2:
#         return "NO"

#     pos1 = x1
#     pos2 = x2
#     diff = abs(pos2 - pos1)

#     while True:


#         pos1 += v1
#         pos2 += v2
#         new_diff = abs(pos2-pos1)

#         if new_diff > diff:
#             return "NO"
#         if new_diff % (diff-new_diff) == 0:
#             return "YES"
#         else:
#             return "NO"

# print(numberLineJumps(43, 2, 70, 2))

# ---------------------------------------------------

# Queens Attack - HackerRank

# def queensAttack(n, k, r_q, c_q, obstacles):

#     v_top = n - r_q
#     v_bot = r_q -1
#     h_right = n - c_q
#     h_left = c_q -1
#     vh_right_bot = min(r_q -1, n -c_q)
#     vh_right_top = min(n-c_q, n-r_q)
#     vh_left_bot = min(c_q, r_q) -1
#     vh_left_top = min(c_q -1, n-r_q)


#     for i in obstacles:
#         row = abs(i[0] - r_q)
#         col = abs(i[1] - c_q)

#         if row == col:
#             # top right
#             if i[0] > r_q and i[1] > c_q and (i[0] - r_q) < vh_right_top:
#                 vh_right_top = i[0] -r_q -1

#             # bot right
#             if i[0] < r_q and i[1] > c_q and (r_q - i[0]) < vh_right_bot:
#                 vh_right_bot = r_q - i[0]-1

#             # top left
#             if i[0] > r_q and i[1] < c_q and (i[0] - r_q) < vh_left_top:
#                 vh_left_top = i[0] - r_q -1

#             # bot left
#             if i[0] < r_q and i[1] < c_q and (r_q - i[0]) < vh_left_bot:
#                 vh_left_bot = r_q - i[0] -1


#         if row == 0:

#             # right
#             if i[1] > c_q and (i[1] - c_q -1) < h_right:
#                 h_right = i[1] - c_q -1

#             # left
#             if i[1] < c_q and (c_q - i[1] -1) < h_left:
#                 h_left = c_q - i[1] -1

#         if col == 0:

#             # top
#             if i[0] > r_q and (i[0] - r_q -1) < v_top:
#                 v_top = i[0] - r_q -1

#             # bot
#             if i[0] < r_q and (r_q - i[0] -1) < v_bot:
#                 v_bot = r_q - i[0] -1

#     return sum([v_top, v_bot, vh_left_bot, vh_right_bot, vh_left_top, vh_right_top, h_left, h_right])


# print(
# queensAttack(4, 0, 4, 4, [])
# )

# ----------------------------------------------------------------------------


# the-quickest-way-up - HackerRank

# def quickestWayUp(ladders, snakes):

#     from collections import deque

#     paths = {}

#     for i in ladders + snakes:
#         paths[i[0]] = i[1]

#     # Initial position and with 0 rolls
#     queue = deque([(1, 0)])
#     visited = set()


#     while len(queue)> 0:

#         pos, roll = queue.popleft()


#         if pos == 100:
#             return roll

#         visited.add((pos, roll))

#         for n in range(1, 7):
#             next = pos + n

#             if (next, roll) in visited or next > 100: continue

#             queue.append((next in paths and paths[next] or next, roll + 1))

#     return -1

# print(
# quickestWayUp([[32, 62], [42, 68], [12, 98]], [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]))

# --------------------------------------------------------------------

# Longest Increasing Subsequence - HackerRank

# 15, 27, 14, 38, 26, 55, 46, 65, 85

# 15
# 15, 27
# 14
# 14 38
# 14, 26
# 14, 26, 55
# 14, 26, 46
# 14, 26, 46, 65, 85

# 15, 27, 50, 18, 19, 26, 89

# 15
# 15, 27
# 15, 27, 50
# 15, 18
# 15, 18, 19
# 15, 18, 19, 26, 89

# def longestIncreasingSubsequence(arr):

#     count = [[arr[0]]]

#     for i in range(1, len(arr)):

#         count.sort(key=lambda item: len(item), reverse= True)

#         for x in range(len(count)):
#             if count[x][len(count[x]) -1] <= arr[i]:
#                 count.append(count[x] + [arr[i]])
#                 break

#             if x == len(count) -1:
#                 count.append([arr[i]])


#     return len(max(count, key = lambda item : len(item)))


# print(
# longestIncreasingSubsequence([21, 22, 23, 24, 25, 1, 2, 3, 4, 100, 27, 28, 29, 30])
# )

# --------------------------------------------------------------------

#  329. Longest increasing path in a matrix - leetcode

# def longestIncreasingPath(matrix):

#     transformations = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#     paths = {}

#     def bfs(node):

#         x, y = node[0], node[1]

#         if (x, y) in paths:
#             return paths[(x, y)]

#         nodes_to_traverse = []

#         for i in transformations:
#             row, col = (x + i[0], y + i[1])

#             if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]) and matrix[row][col] > matrix[x][y]:
#                 nodes_to_traverse.append((row, col))

#         if len(nodes_to_traverse) == 0:
#             paths[(x, y)] = [matrix[x][y]]
#             return [matrix[x][y]]

#         for j in nodes_to_traverse:

#             p = [matrix[x][y]] + bfs(j)

#             if (x, y) in paths:
#                 if len(paths[(x, y)]) < len(p):
#                     paths[(x, y)] = p
#             else:
#                 paths[(x, y)] = p
#         return paths[(x, y)]

#     for r in range(len(matrix)):
#         for c in range(len(matrix[0])):
#             bfs((r, c))

#     return len(max([k for k in paths.values()], key=len))


# print(
# longestIncreasingPath([[1]])
# )

# ---------------------------------------------------------------------

# 647. Palindromic Substrings


# def countSubstring(s):

#     count = 0

#     for i in range(len(s)):

#         for j in range(len(s), i, -1):
#             substring = s[i:j]

#             if substring == substring[::-1]:
#                 count += 1

#     return count

# print(
# countSubstring('aaa'))

# # racecar
# # rwewrdede

# -------------------------------------------------------------

# Torque and Development - HackerRank

# def roadsAndLibraries(n, c_lib, c_road, cities):

#     from collections import defaultdict

#     if c_road > c_lib:
#         return n * c_lib

#     if len(cities) == 0:
#         return n * c_lib

#     p = list(range(n+1))

#     def find(x):
#         if x != p[x]:
#             p[x] = find(p[x])
#         return p[x]

#     def union(x, y):
#         px = find(x)
#         py = find(y)

#         if px != py:
#             p[py] = px

#     for x, y in cities:
#         union(x, y)

#     hash = defaultdict(list)
#     for i, val in enumerate(p):
#         hash[find(val)].append(i)

#     groups = len(hash) -1

#     lone_cities = len([x for x in hash.values() if len(x) == 1]) -1


#     return (groups * c_lib) + ((n-lone_cities-1)*c_road)


# print(roadsAndLibraries(5, 6, 1, [[1, 2], [1, 3], [1, 4]]))

# -------------------------------------------------------------------

# Breadth First Search: Shortest Reach - HackerRank

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

#             for k in nodes[i]:
#                 if p[k] == -1 and k not in next:
#                     next.append(k)
#                     p[k] = (count+1)*6
#         nodes_to_traverse = next
#         count += 1
#     del p[s]
#     return p[1:]

# ------------------------------------------------------------------

# Larry's Array - HackerRank

# Using Parity of Permutations
# If parity is odd then impossible to sort.
# Parity if odd if number of inversions is an odd number.

# def larrysArray(A):

#     inversion = 0

#     for i in range(len(A)):

#         for x in A[i+1:]:

#             if x < A[i]:
#                 inversion += 1

#     if inversion % 2 == 0:
#         return "YES"
#     else:
#         return "NO"

# -------------------------------------------------------------

# Breaking best and worst records - HackerRank


# def breakingRecords(scores):

#     max = scores[0]
#     min = scores[0]

#     count_max = 0
#     count_min = 0

#     for score in scores:
#         if score > max:
#             count_max += 1
#             max = score
#         elif score < min:
#             count_min += 1
#             min = score

#     return [count_max, count_min]


# --------------------------------------------------------------

# Two Pluses Grid - HackerRank

# def twoPluses(grid):

#     from itertools import combinations

#     combos = []

#     def bfs(node):
#         row, col = node[0], node[1]
#         count = [(row, col)]
#         i = 1
#         while True:
#             combos.append(count.copy())
#             top = grid[row + i][col] if row + i < len(grid) else 'B'
#             bot = grid[row - i][col] if row - i >= 0 else 'B'
#             right = grid[row][col +i] if col + i < len(grid[row]) else 'B'
#             left = grid[row][col -i] if col - i >= 0 else 'B'

#             if top == "B" or bot == "B" or left == "B" or right == "B":
#                 break
#             count.extend([(row+i, col), (row-i, col), (row, col+i), (row, col -i)])
#             i+= 1

#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j] == 'G':
#                 bfs([i, j])

#     res = []
#     for a, b in combinations(combos, 2):
#         if set(a).isdisjoint(set(b)):
#             res.append(len(a)*len(b))

#     return max(res) if len(combos) > 0 else 0


# print(
# twoPluses(['GGGGGG', 'GBBBGB', 'GGGGGG', 'GGBBGB', 'GGGGGG'])
#     )


# ------------------------------------------------------------


# Encryption - HackerRank

# def encryption(s):

#     import math

#     str = s.replace(' ', '')
#     string_root = math.sqrt(len(str))
#     n, m = 0, 0

#     if string_root % 1 == 0:
#         n = int(string_root)
#         m = int(string_root)
#     elif string_root % 1 < 0.5:
#         n = math.floor(string_root)
#         m = math.ceil(string_root)
#     else:
#         n = math.ceil(string_root)
#         m = math.ceil(string_root)

#     res = ['' for _ in range(m)]

#     for idx, val in enumerate(str):
#         res[idx%m] += val

#     return ' '.join(res)


# print(
# encryption('wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny')
# )

# -------------------------------------------------------------------------

# // Transpose Matrix - Leetcode

# def transpose(matrix):

#     res = [[0 for m in range(len(matrix))] for n in range(len(matrix[0]))]

#     for i in range(len(matrix)):
#       for j in range(len(matrix[0])):
#           res[j][i] = matrix[i][j]

#     return res

# print(transpose(
# [[1,2,3],[4,5,6]]))

# ------------------------------------------------------------------------

# 160. Intersection fo two linked list - leetcode

# def getIntersectionNode(headA, headB):

#     my_dict = {}

#     nodeA = headA

#     while nodeA:
#         my_dict[nodeA] = nodeA.val
#         nodeA = nodeA.next

#     nodeB = headB
#     while nodeB:
#         if nodeB in my_dict:
#             return nodeB
#         nodeB= nodeB.next

#     return None

# -----------------------------------------------------------------------


# 88. Merge Sorted Array

# def mergeSort(nums1, m, nums2, n):

#     pointer = 0

#     while pointer < len(nums1):
#         if len(nums2) == 0: return nums1
#         if nums2[0] <= nums1[pointer]:
#             nums1.insert(pointer, nums2.pop(0))
#             nums1.pop()
#         pointer += 1

#     if len(nums2) != 0:
#         for i in nums2:
#             nums1.pop()
#         nums1.extend(nums2)

#     return nums1


# print(
# mergeSort([1, 2, 3, 0, 0, 0], 6, [2, 5, 6], 3)
# )

# ------------------------------------------------

# 149. Max Points on a Line - leetcode

# def maxPoints(points):

#     if len(points) ==2: return 2

#     count = 1

#     for i in range(len(points)-2):
#         x1, y1 = points[i][0], points[i][1]
#         my_dict = {}
#         for k in range(i + 1, len(points)):
#             x2, y2 = points[k][0], points[k][1]

#             m = (y2-y1)/(x2-x1) if (x2-x1)!= 0 else float('inf')
#             if m in my_dict:
#                 my_dict[m].append(points[k])
#             else:
#                 my_dict[m] = [points[k]]
#         c = max([len(x) for x in my_dict.values()]) +1
#         if c > count:
#             count = c

#     return count

# print(
# maxPoints([[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]])
# )

# -------------------------------------------------------


# 1658. Minimum Operations to Reduce X to Zero

# def minOperations(nums, target):

#     inverse = sum(nums) - target

#     if inverse == 0: return len(nums)
#     start = 0
#     end = 0
#     count = 0
#     res = 0

#     while end < len(nums):
#         count += nums[end]

#         while count > inverse and start < end:
#             count -= nums[start]
#             start += 1

#         if count == inverse and end-start+1>res:
#             res = end -start +1

#         end += 1
#     if res:
#         return len(nums) - res
#     else:
#         return -1

# print(
# minOperations(
# [3,2,20,1,1,3],10))

# -----------------------------------------------------------------

# 5. Longest Palindromic Substring - leetcode

# def LongestPalindrome(s):

#     res = ''

#     pointer = 0

#     i = 0

#     while i < len(s):


#         for j in range(len(s), pointer, -1):

#             if(s[i:j] == s[i:j][::-1]):
#                 print(res, i , j)
#                 if len(s[i:j])> len(res):
#                     res = s[i:j]
#                     pointer = j
#                 break
#         i += 1

#     return res if len(res) > 0 else s[0]


# print(
# LongestPalindrome("klvxwqyzugrdoaccdafdfrvxiowkcuedfhoixzipxrkzbvpusslsgfjocvidnpsnkqdfnnzzawzsslwnvvjyoignsfbxkgrokzyusxikxumrxlzzrnbtrixxfioormoyyejashrowjqqzifacecvoruwkuessttlexvdptuvodoavsjaepvrfvbdhumtuvxufzzyowiswokioyjtzzmevttheeyjqcldllxvjraeyflthntsmipaoyjixygbtbvbnnrmlwwkeikhnnmlfspjgmcxwbjyhomfjdcnogqjviggklplpznfwjydkxzjkoskvqvnxfzdrsmooyciwulvtlmvnjbbmffureoilszlonibbcwfsjzguxqrjwypwrskhrttvnqoqisdfuifqnabzbvyzgbxfvmcomneykfmycevnrcsyqclamfxskmsxreptpxqxqidvjbuduktnwwoztvkuebfdigmjqfuolqzvjincchlmbrxpqgguwuyhrdtwqkdlqidlxzqktgzktihvlwsbysjeykiwokyqaskjjngovbagspyspeghutyoeahhgynzsyaszlirmlekpboywqdliumihwnsnwjc")
# )

# ------------------------------------------------------------

# def LongestPalindrome(s):

#     def expand(l, r):
#         left = l
#         right = r

#         while left >= 0 and right < len(s) and s[left] == s[right]:

#             left -= 1
#             right += 1

#         return s[left+1:right]

#     res = ''
#     for i in range(len(s)):

#         r1 = expand(i, i)
#         r2 = expand(i, i+1)


#         if len(r1) > len(res):
#             res = r1
#         if len(r2) > len(res):
#             res = r2

#     return res

# print(
# LongestPalindrome("a"))

# -------------------------------------------------------------------

# 143. Reorder List - leetcode

# def reorderList(head):

#     stack = []

#     n = head

#     while node:

#         stack.append(node)

#         node = node.next

#     s = stack.pop(0)

#     i = 1
#     while stack:
#         if i % 2 == 0:
#             s.next = stack.pop(0)
#         else:
#             s.next = stack.pop()
#         s=s.next
#         i += 1

#     s.next = None
#     return head

# 0, 1, 2, 3, 4, 5, 6
# 0 -> 6

# -----------------------------------------------------------------

# 4. Median of Two Sorted Arrays - leetcode

# def findMedianSortedArrays(nums1, nums2):

#     target = max(nums1[len(nums1 -1), nums2[len(nums2) -1]])

#     start = 0
#     end = len(nums1) -1

#     res = []


#     while start < end:
#         mid = round(start+end/2)

#         if nums1[mid] > target:
#             start = mid + 1
#         else:
#             end = mid - 1

#     res.append(nums1[mid])

# --------------------------------------------------------------

# x = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

# def t(match):

#     for i in range(len(x)):

#         for k in range(len(x[i])):

#             print(k)

#             if match[k] != None:
#                 if match[k] != x[i][k]:
#                     break
#             else:
#                 continue

#         return i

#     return None

# print(t([6, 7, 8, 9, 10]))


# -------------------------------------------------------------

# 509. Fibonacci Number - leetcode
# Memoization

# def fibMemo(n):

#     hash = {}

#     def r(n):
#         if n in hash:
#             return hash[n]
#         if n <= 1:
#             return n
#         else:
#             hash[n] = r(n-1) + r(n-2)
#             return hash[n]

#     return r(n)


# ----------------------------------------------------------

# 36. Valid Sudoku - leetcode


# def validSudoku(bo):
#     def checkRow():
#         for row in bo:
#             r = list(filter(lambda num: num != ".", row))
#             if len(r) != len(set(r)):
#                 return False
#         return True

#     def checkCol():
#         for col in range(len(bo)):
#             column = []
#             for row in range(len(bo)):
#                 if bo[row][col] != ".":
#                     column.append(bo[row][col])

#             if len(column) != len(set(column)):
#                 return False
#         return True

#     def checkBox():
#         for i in range(3):
#             group = bo[i * 3 : (i * 3) + 3]
#             s1 = list(
#                 filter(
#                     lambda num: num != ".",
#                     [e for sublist in [x[0:3] for x in group] for e in sublist],
#                 )
#             )
#             s2 = list(
#                 filter(
#                     lambda num: num != ".",
#                     [e for sublist in [x[3:6] for x in group] for e in sublist],
#                 )
#             )
#             s3 = list(
#                 filter(
#                     lambda num: num != ".",
#                     [e for sublist in [x[6:9] for x in group] for e in sublist],
#                 )
#             )

#             if (
#                 len(s1) != len(set(s1))
#                 or len(s2) != len(set(s2))
#                 or len(s3) != len(set(s3))
#             ):
#                 return False
#         return True

#     if checkRow() and checkCol() and checkBox():
#         return True
#     else:
#         return False


# bo1 = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]

# bo2 = [
#     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]

# print(validSudoku(bo1))
# print(validSudoku(bo2))


# --------------------------------------------------------------

# 3D surface area - hackerrank


# def surfaceArea(A):

#     s = len(A) * len(A[0]) * 2

#     for r in range(len(A)):
#         for c in range(len(A[r])):
#             num = A[r][c]
#             left = A[r][c - 1] if c - 1 >= 0 else 0
#             right = A[r][c + 1] if c + 1 < len(A[r]) else 0

#             if num > left:
#                 s += num - left

#             if num > right:
#                 s += num - right

#     for c in range(len(A[0])):
#         for r in range(len(A)):
#             num = A[r][c]
#             top = A[r - 1][c] if r - 1 >= 0 else 0
#             bot = A[r + 1][c] if r + 1 < len(A) else 0

#             if num > top:
#                 s += num - top

#             if num > bot:
#                 s += num - bot

#     return s


# print(surfaceArea([[1, 3, 4], [2, 2, 3], [1, 2, 4]]))


# ------------------------------------------------------------

# 1696. Jump Game VI - leetcode


# def jumpGame(nums, k):

#     i = len(nums) - 1
#     count = nums[i]

#     while i > 0:

#         max_num = float("-inf")
#         max_index = None

#         for j in range(i - 1, i - k - 1, -1):

#             if nums[j] > max_num:
#                 max_num = nums[j]
#                 max_index = j

#             if j == 0:
#                 count += nums[j]
#                 return count

#             if nums[j] > 0:
#                 count += nums[j]
#                 i = j
#                 break
#         else:
#             i = max_index
#             count += max_num

#     return count


# print(jumpGame([40, 30, -100, -100, -10, -7, -3, -3], 2))

# 1, -8, -29, -25, 10


# --------------------------------------------------------------

# Fraudulent Activity Notifications - HackerRank


# def activityNotifications(expenditure, d):

#     count = 0

#     for i in range(len(expenditure) - d):
#         te = sorted(expenditure[i : i + d])
#         median = (
#             2 * te[int(len(te) / 2)]
#             if (d / 2) % 2 != 0
#             else (te[int(len(te) / 2)] + te[int((len(te) / 2)) - 1])
#         )
#         curr_num = expenditure[i + d]

#         print(te, median, curr_num)

#         if curr_num >= median:
#             count += 1

#     return count


# print(activityNotifications([10, 20, 10, 40, 50, 60, 10, 30, 35, 36], 4))
# 1, 2, 2, 3, 6, 4

# --------------------------------------------------------------------

# Fraudulent Activity Notifications - HackerRank
# Counting Sort


def activityNotifications(expenditure, d):
    def median(frequency):

        count = 0
        d_median = int(d / 2)
        if d % 2 != 0:
            for idx, val in enumerate(frequency):
                count += val
                if count > d_median:
                    return idx * 2
        else:
            nums = []
            for idx, val in enumerate(frequency):
                count += val
                if count == d_median and len(nums) == 0:
                    nums.append(idx)

                if count > d_median:
                    if len(nums) > 0:
                        nums.append(idx)
                        return sum(nums)
                    else:
                        return idx * 2

    count = 0

    f = [0 for i in range(201)]

    for i in range(d):
        f[expenditure[i]] += 1

    for j in range(d, len(expenditure)):

        print(expenditure[j], median(f))

        if expenditure[j] >= median(f):
            count += 1

        f[expenditure[j]] += 1
        f[expenditure[j - d]] -= 1

    return count


print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
