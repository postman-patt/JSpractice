
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

from collections import defaultdict
from turtle import xcor


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

=======
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

#bigger is greater - HackerRank

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

def steadyGene(gene):

    hash_gene = {'A': 0, 'G': 0, 'T': 0, 'C': 0, }
    hash_pattern = {'A': 0, 'G': 0, 'T': 0, 'C': 0, }
    n = len(gene)/4

    for i in gene:
        hash_pattern[i] += 1

    for key, value in hash_pattern.items():
        if value >= n:
            hash_pattern[key] -= n
        else:
            hash_pattern[key] = 0

    s_len = len(gene)
    p_len = sum([nums for nums in hash_pattern.values()])

    if p_len == 0:
        return 0

    start, start_index, min_len = 0, -1, s_len

    count = 0

    for idx, i in enumerate(gene):

        hash_gene[i] += 1

        if hash_gene[i] <= hash_pattern[i]:
            count += 1

        if count == p_len:

            while (hash_gene[gene[start]] > hash_pattern[gene[start]]) or hash_pattern[gene[start]] == 0:

                if hash_gene[gene[start]] > hash_pattern[gene[start]]:
                    hash_gene[gene[start]] -= 1

                start += 1

            len_window = idx - start + 1

            if min_len > len_window:
                min_len = len_window
                start_index = start

    if start_index == -1:
        return len(gene)

    return min_len


print(
    steadyGene('TATATAGCTTGTCTCCCTAATGTTAGTTCATGCTCGTAAGAGAACTTAGCCTACTAGGACGAGAGAACCGCACGGCGTCGTGAGGTATTTTTCGTAGGACACGCCAGATAGACGGTGGCAATGCCCGTTCAATATGACGCGATGTACGGCTAATGGGAACACTGCCCGACGCGTCTTTAGGACTGTGAGTTGCGGGTTACAGCTATGGTCTTATTGGTATCCGGCCCCTTTCGAGTCGCGATGCGCCTGCCACCACGATATTCGCCCGAAACGCGATTTGTGGGCGAGGTAGTCGTGTTCAACCCTGTAAATTTCCCTAGGTATAATCGTTCTAAGGTTCGCACATACACATCCACACCTACCTTTACACAGTTCGAGGTTCTATACGTCCTCTGAGTGCGTGTTAACACGCCCGTAAATGGGCATTTGGAGTCAGACCAGTACTTTGCGATAAACTTTACTTCCGCGAGACCTGTCCCTGGAACCCTGTTGTAAGGGTTAGGGTTTAATAGCTCCATGTCGTGTGCCTATAAGAAAAGGACGAATGGTGACAGTCCGGCTTAGCCAGGACAATGCGTGGCTGACGACGTCCAGGGTAAATTGAGTTGAATTCGCCTAATTTTAGGGTGTCTTGGTTCAATGAGGTGTCGACTTAACAAAAGGCGACATCAGTTGTCATCTTGCCTTGATAAAGTAAAACACGTGAATAGCCTATCCGGTCTGACCCCCGGGCCATGTGCTTCACCCAGGGAGCATCGCCGCTCTAGAGACGGTGTTCGTAGTCTCGATAACATGTGGGGTAATATAGAATATCCAAGACCGGTAGGAGGGGCGGTTCCGCGTCATAAGAAGTCCCAACGTGGCCTGCCACGTTCAAACAGGATACGCTATAACAGCTTCGTGGGTAATTGATGGATACGCCCGCAGGCTACCCATGCTCTTGCGATTTTGCAACCCTCGGAACCGTCACTCGTACACCCAGACATCATCTCATACAATTGCCTCACCTTCATGCCGGTACATAGGTGCCATCTCCGCTTAAGAATCCTCGCAGCAATTAATGTGACAGCACGCTAGTCCACTAGCGTATGATTACGCCACCGGGCCACCATGGACAAAAACGTTGAATTCCGACTAATAGACGAGTGTCCGATCGGGTCAACCGATCTCGGATGTTGCGTACCAGGACTACTGGGCTCGGGCCGAATCAGACACACGTATGCAACAGATACCGATAGGCGTCTTCCTAAGTAACAGCCGTAATCAATGGTGCCACAGATCTACTAATTACGGTGAAGATCATGGCCCACGACGCTGTACGGGTTTATAGCTGCCACAAACTTTAGGAAGTTTCAGCAATCGACGCGTAGTATGTGTGCTCAGACGGGTCGAGCATGCACTTGTGTATTAAGTTACTTGGCTGAACAACCTGTTGATAGATCTTGAGAGGACCGAGAAATTGCCCTCCGGTTATGAAACAGGTCCTGCGTACCAATCCTT')
)

