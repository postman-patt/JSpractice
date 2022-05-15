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
