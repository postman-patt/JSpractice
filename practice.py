# def number_length(n):
#     count = 0
#     for i in str(n):
#         count += 1
#     print(count)


# number_length(123423435)

# -----------------------
# Pentagonal Number
# def pentagonal(n):
#     count = 1
#     for i in range(n):
#         count += i * 5
#     print(count)


# pentagonal(3)
# pentagonal(8)

# ----------------------


# def number_length(num):

#     print(len(str(num)))


# number_length(21344)

# ---------------------


# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 != 0:
#         print("Fizz")
#     elif num % 5 == 0 and num % 3 != 0:
#         print("Buzz")
#     elif num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(str(num))


# fizz_buzz(5)

# -----------------------

# import math


# def square_areas_differences(num):
#     outerSquareArea = (num * 2) ** 2
#     innerSquareArea = math.sqrt(((num * 2) ** 2) / 2) ** 2
#     return round(outerSquareArea - innerSquareArea, 1)


# print(square_areas_differences(5))
# print(square_areas_differences(6))


# -------------------------------


# def is_adjacent(matrix, node1, node2):
#     if matrix[node1][node2] == 1:
#         return True
#     else:
#         return False


# matrix1 = [
#     [0, 1, 0, 1, 1],
#     [1, 0, 1, 0, 0],
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 0, 1],
#     [1, 0, 0, 1, 0],
# ]

# matrix2 = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]

# print(is_adjacent(matrix1, 1, 4))
# print(is_adjacent(matrix2, 0, 1))
# print(is_adjacent(matrix2, 0, 2))

# -------------------------------

# sampleList = ["cow", "pig", "cow", "cow"]
# sampleList2 = ["table", "table", "table"]
# samplelist3 = ["chair", "pencil", "arm"]


# def pluralize(lst):
#     plurals = set()

#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             if lst[i] == lst[j] and i != j:
#                 plurals.add(lst[i] + "s")

#     for i in range(len(lst)):
#         if lst[i] + "s" not in plurals:
#             plurals.add(lst[i])
#     return plurals


# print(pluralize(sampleList))
# print(pluralize(sampleList2))
# print(pluralize(samplelist3))

# -----------------------------------


# def addTwoNumbers(l1, l2):
#     stringl1 = ""
#     stringl2 = ""
#     for i in range(len(l1) - 1, -1, -1):
#         stringl1 += str(l1[i])

#     for i in range(len(l2) - 1, -1, -1):
#         stringl2 += str(l2[i])

#     answer = [int(d) for d in reversed(str(int(stringl1) + int(stringl2)))]

#     return answer


# list1 = [2, 4, 3]
# list2 = [5, 6, 4]

# print(addTwoNumbers(list1, list2))

# -------------------------------------


# def uncensor(string, vowels):
#     if string.find("*") == -1:
#         return string
#     else:
#         vowelList = list(vowels)
#         vowelsList2 = ""
#         newString = string.replace("*", vowelList.pop(0), 1)
#         return uncensor(newString, vowelsList2.join(vowelList))


# print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
# print(uncensor("abcd", ""))
# print(uncensor("*PP*RC*S*", "UEAE"))

# -----------------------------------


# def is_disarium(num):
#     numArray = []
#     count = 0
#     for n in str(num):
#         numArray.append(int(n))
#     for i in range(len(numArray)):
#         count += numArray[i] ** (i + 1)
#     if count == num:
#         return True
#     else:
#         return False


# print(is_disarium(75))
# print(is_disarium(6))

# ----------------------------------

# d1 = {"z": "q", "w": "f"}
# d2 = {"a": 1, "b": 2, "c": 3}
# d3 = {"zebra": "koala", "horse": "camel"}


# def invert(dict):
#     newDict = {}
#     for key in dict:
#         newDict[dict[key]] = key
#     return newDict


# print(invert(d1))
# print(invert(d2))
# print(invert(d3))

# -----------------------------------


# def bonus(num):
#     result = 0

#     if 32 < num < 40:
#         result += (num - 32) * 325
#     elif num > 40:
#         result += 8 * 325

#     if 40 < num < 48:
#         result += (num - 40) * 550
#     elif num > 48:
#         result += 8 * 550

#     if num > 48:
#         result += (num - 48) * 600

#     return result


# print(bonus(15))

# print(bonus(37))

# print(bonus(50))

# ----------------------------------------------------


# def tallest_skycraper(List):
#     for i in range(len(List)):
#         for j in List[i]:
#             if j == 1:
#                 return len(List) - i


# print(tallest_skycraper([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]))
# print(tallest_skycraper([[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]))
# print(tallest_skycraper([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]))

# -----------------------------------------------------
# import math

# a1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# a2 = [50, 20, 30, 90, 30, 20, 50, 20, 90]
# a3 = []


# def sock_merchant(array):
#     uniqueSocks = set(array)
#     result = 0
#     for i in uniqueSocks:
#         sockCount = 0
#         for j in array:
#             if i == j:
#                 sockCount += 1
#         result += math.floor(sockCount / 2)
#     return result


# print(sock_merchant(a1))
# print(sock_merchant(a2))
# print(sock_merchant(a3))

# ----------------------------------------


# def consecutive_combo(ar1, ar2):
#     arr = ar1 + ar2
#     arr.sort()

#     result = True

#     for i in range(len(arr) - 1):
#         if arr[i + 1] - arr[i] != 1:
#             result = False

#     return result


# print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
# print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
# print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
# print(consecutive_combo([44, 46], [45]))

# ------------------------------------------

# import socket


# def get_domain(str):
#     a = socket.gethostbyaddr(str)[0]
#     return a


# print(get_domain("8.8.8.8"))

# -------------------------------------------

# import itertools as it


# def permutations(str):
#     return " ".join(sorted("".join(p) for p in it.permutations(str)))

# print(permutations("AB"))
# print(permutations("CD"))
# print(permutations("EF"))
# print(permutations("NOT"))
# print(permutations("RAM"))
# print(permutations("YAW"))

# --------------------------------------------

# import math


# def shift_to_right(num1, num2):
#     return math.floor(num1 / (2 ** num2))


# import math


# def shift_to_right2(num1, num2):
#     if num2 != 0:
#         return shift_to_right2(num1 / 2, num2 - 1)
#     else:
#         return math.floor(num1)


# print(shift_to_right2(80, 3))
# print(shift_to_right2(-24, 2))

# ----------------------------------------------


# def is_harshad(num):
#     count = 0
#     for x in [int(i) for i in str(num)]:
#         count += x

#     if num % count == 0:
#         return True
#     else:
#         return False


# print(is_harshad(75))
# print(is_harshad(171))
# print(is_harshad(481))
# print(is_harshad(89))
# print(is_harshad(516))

# ---------------------------------------------

# import re


# def is_valid_hex_code(str):
#     if len(str) == 7:
#         if re.match("#([a-f A-F 0-9]{6})", str) != None:
#             return True
#         else:
#             return False
#     else:
#         return False


# print(is_valid_hex_code("#CD5C5C"))
# print(is_valid_hex_code("#CD5C5Z"))

# -------------------------------------------

# import re


# def same_length(str):
#     import re

#     regex = "([1]*)([0]*)"
#     result = list(filter(None, re.split(regex, str)))
#     isValid = True
#     if len(result) % 2 != 0:
#         return False
#     for i in range(0, len(result) - 1, 2):
#         if len(result[i]) != len(result[i + 1]):
#             isValid = False
#     return isValid


# print(same_length("110011100010"))
# print(same_length("101"))

# ------------------------------------------


# def fair_swap(list1, list2):
#     result = set()
#     for i in range(len(list1)):

#         for j in range(len(list2)):

#             newList1 = list1.copy()
#             newList2 = list2.copy()
#             num1 = newList2.pop(j)
#             num2 = newList1.pop(i)
#             newList1.append(num1)
#             newList2.append(num2)
#             count1 = 0
#             count2 = 0
#             for x in newList1:
#                 count1 += x
#             for y in newList2:
#                 count2 += y

#             if count1 == count2:
#                 result.add((list1[i], list2[j]))

#     return result


# print(fair_swap([1, 1], [2, 2]))

# --------------------------------------------

# def fair_swap(list1, list2):
#     result = set()
#     l1_sum = sum(list1)
#     l2_sum = sum(list2)

#     for num1 in set(list1):
#         for num2 in set(list2):
#             if l1_sum - num1 + num2  == l2_sum - num2 + num1:
#                 result.add((num1, num2))

#     return result

#     return result

# ------------------------------------------


# def remove_letters(letters, word):
#     result = letters.copy()
#     for i in word:
#         if i in result:
#             result.remove(i)
#     return result


# print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
# print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))
# print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))


# -------------------------------------------


# def loves_me(num):
#     result = []
#     for i in range(num):
#         if i + 1 == num:
#             if i % 2 == 0 or i == 0:
#                 result.append("LOVES ME")
#             else:
#                 result.append("LOVES ME NOT")
#         elif i % 2 == 0 or i == 0:
#             result.append("loves me")
#         else:
#             result.append("loves me not")
#     return ", ".join(result)


# print(loves_me(3))

# -------------------------------------------

# import datetime


# def has_friday_13(month, year):
#     x = datetime.datetime(year, month, 13)
#     if x.strftime("%a") == "Fri":
#         return True
#     else:
#         return False


# print(has_friday_13(3, 2020), has_friday_13(10, 2017), has_friday_13(1, 1985))


# --------------------------------------------


# def find_the_difference(str1, str2):
#     string1 = sorted(str1)
#     string2 = sorted(str2)

#     if len(str1) == 0:
#         return str2
#     for i in range(len(string1)):
#         if string2[i] != string1[i]:
#             return string2[i]
#     return string2[len(str2) - 1]


# find_the_difference("abcd", "abcde")
# find_the_difference("", "y")
# find_the_difference("ae", "aea")

# best way
# def find_the_difference(s, t):
#     for i in s:
#         t = t.replace(i, "", 1)
#     return t

# -------------------------------------------


# def parse_code(str):
#     newString = list(filter(None, str.split("0")))

#     return dict(
#         {"first_name": newString[0], "last_name": newString[1], "id": newString[2]}
#     )


# parse_code("John000Doe000123")

# ----------------------------------------
# l1 = [1, 2, 4, 5, "d"]
# l2 = [1]


# def cycle(list):
#     n1 = list.pop(0)
#     list.append(n1)


# cycle(l1)
# print(l1)
# print(l1[0])

# cycle(l2)
# print(l2)
# print(l2[0])

# -----------------------
# def middle_words(list):
#     if len(list) % 2 == 0:
#         print(len(list) / 2)
#         return [list[int(len(list) / 2) - 1], list[int(len(list) / 2)]]
#     else:
#         return [list[int(len(list) / 2)]]


# l1 = ["hello", "hi", "cool", "yes"]


# def longest_sentence(str):
#     return sorted(str.split("."), key=len, reverse=True)[0]


# def long_high_word(wordlist):
#     return sorted(wordlist, key=lambda item: (len(item), item), reverse=True)[0]


# print(long_high_word(["a", "cat", "sat"]))

# print(longest_sentence("hello. my name is the. what is it with you"))def middle_words(list):
#     if len(list) % 2 == 0:
#         print(len(list) / 2)
#         return [list[int(len(list) / 2) - 1], list[int(len(list) / 2)]]
#     else:
#         return [list[int(len(list) / 2)]]


# l1 = ["hello", "hi", "cool", "yes"]


# def longest_sentence(str):
#     return sorted(str.split("."), key=len, reverse=True)[0]


# def long_high_word(wordlist):
#     return sorted(wordlist, key=lambda item: (len(item), item), reverse=True)[0]


# print(long_high_word(["a", "cat", "sat"]))

# print(longest_sentence("hello. my name is the. what is it with you"))

# ------------------------------------------


# def valid_word_nest(word, nest):
#     import re

#     if len(re.findall(word, nest)) > 1:
#         return False
#     if nest.find(word) == -1:
#         return False
#     else:
#         if len(word) == len(nest):
#             return True
#         else:
#             wordIndex = nest.find(word)
#             newNest = nest[0:wordIndex] + nest[wordIndex + len(word) :]
#             return valid_word_nest(word, newNest)


# print(valid_word_nest("broadcast", "broadcast"))

# -------------------------------------------------


# def hangman(str, array):

#     return "".join(
#         [char if char in array else " " if char == " " else "-" for char in str]
#     )


# print(hangman("helicopter", ["o", "e", "s"]))

# ------------------------------------


# def top5_words(text):

#     tally = {}
#     text_list = text.split()
#     empty_list = []
#     new_tally = {}

#     for word in text_list:
#         if word in tally:
#             tally[word] -= 1
#         else:
#             tally[word] = -1

#     sorted_keys = sorted(tally, key=lambda item: (tally[item], item))
#     for word in sorted_keys:
#         new_tally[word] = tally[word]

#     return list(new_tally.keys())[:5]


# print(top5_words("one one was a racehorse two two was one too"))
# print(top5_words("the quick brown fox jumped over the lazy dog"))

# --------------------------------------------


# def rearranged_difference(num):
#     return int("".join(sorted([n for n in str(num)], reverse=True))) - int(
#         "".join(sorted([n for n in str(num)]))
#     )


# print(rearranged_difference("4837249073"))

# --------------------------------------------

# If you update dictionary you can also instantiate a new property of the object. The __dict__ is where the listing of all properties of the object are stored.
# class Employee:
#     def __init__(self, fullName, **kwargs):
#         self.name = fullName.split(" ")[0]
#         self.lastname = fullName.split(" ")[1]
#         self.__dict__.update(kwargs)

#     def showDict(self):
#         print(self.__dict__)


# patrick = Employee("Patrick Vuong", salary=100000)

# patrick.showDict()

# -----------------------------------------------


# def group(arr, size):
#     import math

#     result = [[] for x in range(math.ceil(len(arr) / size))]
#     for i in range(len(arr)):
#         if i < len(result):
#             result[i].append(arr.pop(0))
#         else:
#             result[i % len(result)].append(arr.pop(0))
#     return result


# print(group([1, 2, 3, 4, 5, 6, 7], 4))

# --------------------------------------------


# import pickle


# class Selfie:
#     def __init__(self):
#         self.lst_state = []

#     def save_state(self):
#         self.lst_state.append(pickle.dumps(self))

#     def recover_state(self, n):
#         if 0 <= n < len(self.lst_state):
#             obj = pickle.loads(self.lst_state[n])
#             obj.lst_state = self.lst_state
#             return obj
#         return self

#     def n_states(self):
#         return len(self.lst_state)


# d = Selfie()


# -------------------------------------------------------


# def id_matrix(num):
#     if type(num) != int:
#         return "Error"

#     result = [[] for x in range(abs(num))]
#     count = 0 if num >= 0 else abs(num) - 1
#     for i in range(abs(num)):
#         for j in range(abs(num)):
#             if count == j:
#                 result[i].append(1)
#             else:
#                 result[i].append(0)
#         if num > 0:
#             count += 1
#         else:
#             count -= 1
#     return result


# print(id_matrix("buggy"))

# ------------------------------------------------------

# 0, 1, 1, 2, 3, 5, 8, 13


# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)


# print(fib(5))

# -------------------------------------------------------

# sample = [["!!!", "O", "!"], ["X", "#", "!!!"], ["!!", "X", "O"]]


# def check_score(s):
#     matrix = {"#": 5, "O": 3, "X": 1, "!": -1, "!!": -3, "!!!": -5}

#     count = 0

#     for i in s:
#         for j in i:
#             for x in matrix:
#                 if j == x:
#                     count += matrix[x]

#     if count < 0:
#         return 0
#     else:
#         return count


# print(check_score(sample))

# ---------------------------------------------------------


# class equals:
#     def __eq__(self, other):
#         return True

# ------------------------------------------


# def non_increasing_tst(ts, delta):
#     # TODO
#     i = 0
#     Answer = True
#     while i + 1 < len(ts):
#         if ts[i + 1] - ts[i] > delta:
#             Answer = False
#             break
#         i += 1

#     return Answer


# non_increasing_tst([100, 90, 80, 70, 70, 60], 0)

# ---------------------------------------------


# def pattern_check(lst, pattern, delta):

#     result = ""
#     for i in range(len(lst) - 1):
#         if abs(lst[i + 1] - lst[i]) <= delta:
#             result += "s"
#             continue
#         elif lst[i + 1] - lst[i] > delta:
#             result += "u"
#             continue
#         else:
#             result += "d"
#             continue

#     print(result)

#     if result.find(pattern) != -1:
#         return True
#     else:
#         return False


# print(
#     pattern_check([58, 54, 54, 52, 54, 50, 47], "sdud", 0),
#     pattern_check([58, 54, 54, 52, 54, 50, 47], "sdud", 2),
#     pattern_check([58, 54, 54, 52, 54, 50, 47], "sss", 2),
#     pattern_check([58, 54, 54, 52, 54, 50, 47], "dd", 0),
#     pattern_check([1, 2, 1, 8, 1, 2], "udud", 0),
#     pattern_check([1, 2, 1, 8, 1, 2], "udud", 2),
# )


# --------------------------------------


# def closest_tst(ts, lstTs):

#     # Instantiate list containing the distances of each element in lstTs
#     result = []

#     for i in lstTs:
#         # Instantiate list containing the diff between each list AND the primary Ts
#         diff = []
#         for j in range(len(i)):
#             diff.append(abs(ts[j] - i[j]))

#         # Applying the formula
#         mean = sum(diff) / len(i)

#         # The section of the formula that requires you to sum the values
#         count = 0
#         for x in diff:
#             count += (x - mean) ** 2
#         # Calculate distance with you summed value
#         distance = (count / len(i)) ** 1 / 2

#         # Once distance is found between the primary list and an element in lstTs we append the result to result
#         result.append(distance)

#         # Finds the index of the smallest value
#     return result.index(sorted(result)[0])


# # Primary
# ts1 = [10, 10, 10, 10]


# ts2 = [10, 10, 20, 20]
# ts3 = [0, 0, 40, 40]
# ts4 = [100, 100, 100, 100]
# ts5 = [10, 10, 20, 10]
# print(closest_tst(ts1, [ts2, ts5]))


# def anomaly_tst(ts, w, threshold):

#     subsequences = [[x for x in ts[i : i + w]] for i in range(len(ts) - w + 1)]

#     meanDistanceOfSubseuquences = []

#     def distance(ts1, ts2):
#         count = 0
#         for i in range(len(ts1)):
#             count += abs(ts1[i] - ts2[i]) ** 2
#         return count ** 0.5

#     for i, sub1 in enumerate(subsequences):
#         distSubsequences = []
#         for j, sub2 in enumerate(subsequences):
#             if i != j:
#                 distSubsequences.append(distance(sub1, sub2))
#         meanOfSubsequence = sum(distSubsequences) / len(distSubsequences)
#         meanDistanceOfSubseuquences.append(meanOfSubsequence)

#     # for k, value in enumerate(meanDistanceOfSubseuquences):
#     #     if value > threshold:
#     #         return k
#     if max(meanDistanceOfSubseuquences) > threshold:
#         return meanDistanceOfSubseuquences.index(max(meanDistanceOfSubseuquences))

#     return -1


# ts = [3, 0, 2, 40, 1]
# print(anomaly_tst([10, 10, 10, 10, 0, 0, 10], 2, 12))
# print(anomaly_tst([10, 10, 10, 10, 10, 10, 10], 3, 12))
# print(anomaly_tst(ts, 2, 40))
# print(anomaly_tst(ts, 2, 100))
# print(anomaly_tst([3, 0, 2, 40, 11], 3, 14))

# -----------------------------------------------------------------------

# import math


# def anomaly_tst(ts, w, threshold):
#     number2 = 0

#     average_distance = list()

#     # cycles through the subsequences
#     while number2 < (len(ts) - (w - 1)):
#         distance_list = list()
#         subsequence1 = ts[number2 : w + number2]
#         number2 += 1
#         number3 = 0

#         while number3 < (len(ts) - (w - 1)):

#             subsequence2 = ts[number3 : w + number3]
#             print(subsequence1, subsequence2)
#             number3 += 1
#             distance = math.sqrt(
#                 (subsequence1[0] - subsequence2[0]) ** 2
#                 + (subsequence1[1] - subsequence2[1]) ** 2
#             )
#             distance_list.append(distance)

#         average_distance.append(sum(distance_list) / 3)

#     if max(average_distance) > threshold:
#         return average_distance.index(max(average_distance))

#     return -1


# ts = [3, 0, 2, 40, 1]
# # print(anomaly_tst([10, 10, 10, 10, 0, 0, 10], 2, 12))
# # print(anomaly_tst([10, 10, 10, 10, 10, 10, 10], 3, 12))
# # print(anomaly_tst(ts, 2, 40))
# # print(anomaly_tst(ts, 2, 100))
# print(anomaly_tst([3, 0, 2, 40, 1], 3, 14))

# ------------------------------------------------------------------------


# def basenum(num, base):
#     def create_generator():
#         for i in range(len(str(num))):
#             yield i

#     generator = create_generator()
#     for x in generator:
#         if base < int(str(num)[x]):
#             return False
#     return True


# print(basenum(1232614, 5))

# ---------------------------------------------------------------------------


# def basenum(num, base):
#     def conver(n, b):
#         a = 0
#         i = 0
#         while n:
#             n, r = divmod(n, b)
#             a += 10 ** i * r
#             i += 1

#         return a

#     for i in range(num + 1):
#         if conver(i, base) == num:
#             return True
#         elif i == num & base == 10:
#             return True
#     return False


# print(basenum(1012121211212, 2))


# def conver(n, b):
#     a = 0
#     i = 0
#     while n:
#         n, r = divmod(n, b)
#         a += 10 ** i * r
#         i += 1

#     return print(type(a))


# conver(10, 9)


# def basenum(num, base):

#     n1 = str(num)
#     length = len(n1)
#     for i in range(length):
#         if base <= int(n1[i]):
#             return False
#     return True


# print(basenum(0, 0))

# --------------------------------------------------------------


# def matching_codons(complements, pool1, pool2):

#     result = []

#     for i in pool1:
#         complement = ""
#         for k in i:
#             complement += complements[k]

#         for j in pool2:
#             if complement == j:
#                 result.append((i, j))

#     return result


# def matching_codons(complements, pool1, pool2):
#     match = []
#     compare_lst = []
#     result = []
#     for codon1 in pool1:
#         for nucleotides in codon1:
#             match.append(complements[nucleotides])
#     for i in range(len(match) - 2):
#         codon = match[i] + match[i + 1] + match[i + 2]
#         compare_lst.append(codon)

#     for codon2 in pool2:
#         if codon2 in compare_lst:
#             result.append(codon2)
#     return result


# complements = {"A": "T", "C": "G", "T": "A", "G": "C"}
# p1 = ["AAG", "TAC", "CGG", "GAT", "TTG", "GTG", "CAT", "GGC", "ATT", "TCT"]
# p2 = ["TAA", "CTA", "AAC", "TTC", "AGA", "CCC", "CCG", "GTA"]

# print(matching_codons(complements, p1, p2))

# ----------------------------------------------------


# def add(n):
#     if n > 100:
#         return print("Finished")
#     else:
#         print(n)
#         return add(n + n)


# add(5)


# -----------------------------------------------------------

# def super_digit(n, k):
#     if len(n) == 1:
#         return int(n)
#     else:
#         sumNum = sum([int(x) for x in (k * n)])
#         return super_digit(str(sumNum), 1)


# print(super_digit("148", 3))


# ------------------------------------------------------------------


# def reverse(x):
#     result = [i for i in str(abs(x))]
#     if x < 0:
#         result.reverse()
#         result.insert(0, "-")
#         result = int("".join(result))
#     else:
#         result.reverse()
#         result = int("".join(result))

#     if -(2 ** 31) < result < ((2 ** 31) - 1):
#         return result
#     else:
#         return 0


# print(reverse(213123))

# --------------------------------------------------------------------


# def atbash(code):
#     cipher = [
#         "a",
#         "b",
#         "c",
#         "d",
#         "e",
#         "f",
#         "g",
#         "h",
#         "i",
#         "j",
#         "k",
#         "l",
#         "m",
#         "n",
#         "o",
#         "p",
#         "q",
#         "r",
#         "s",
#         "t",
#         "u",
#         "v",
#         "w",
#         "x",
#         "y",
#         "z",
#     ]

#     result = ""
#     for x in range(len(code)):
#         if code[x].lower() in cipher:
#             if code[x].isupper():
#                 result += cipher[
#                     len(cipher) - cipher.index(code[x].lower()) - 1
#                 ].upper()
#             else:
#                 result += cipher[len(cipher) - cipher.index(code[x].lower()) - 1]
#         else:
#             result += code[x]

#     return result


# print(atbash("apple"))
# print(atbash("Hello world!"))
# print(atbash("Christmas is the 25th of December"))

# -----------------------------------------------------------------


# def knightBFS(x1, y1, x2, y2):
#     start = (x1, y1)
#     end = (x2, y2)
#     queue = [[start]]

#     def adj(node):
#         adjacentNodes = []
#         moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
#         for x in moves:
#             if (
#                 node[0] + x[0] >= 1
#                 and node[0] + x[0] <= 8
#                 and node[1] + x[1] >= 1
#                 and node[1] + x[1] <= 8
#             ):
#                 transNode = tuple(map(lambda i, j: i + j, x, node))
#                 if (
#                     transNode not in [a for item in queue for a in item]
#                     and transNode not in adjacentNodes
#                 ):
#                     adjacentNodes.append(transNode)
#         return adjacentNodes

#     for i, value1 in enumerate(queue):
#         sublist = []
#         for value2 in value1:
#             if value2 == end:
#                 return i
#             else:
#                 sublist += adj(value2)
#         queue.append(sublist)


# print(knightBFS(8, 8, 3, 3))

# What is a better way of keeping track of which layer you are on in BFS?

# -----------------------------------------------------------------------------


# def numgrid(grid):
#     def adj(node):
#         adjacentNodes = []
#         transformations = [
#             (0, 1),
#             (1, 1),
#             (0, -1),
#             (-1, -1),
#             (-1, 0),
#             (1, 0),
#             (-1, 1),
#             (1, -1),
#         ]
#         for x in transformations:
#             if (
#                 node[0] + x[0] >= 0
#                 and node[0] + x[0] <= len(grid[0]) - 1
#                 and node[1] + x[1] >= 0
#                 and node[1] + x[1] <= len(grid) - 1
#             ):
#                 adjacentNodes.append(tuple(map(lambda i, j: i + j, x, node)))
#         return adjacentNodes

#     for index_I, i in enumerate(grid):
#         for index_J, j in enumerate(i):
#             pos = (index_I, index_J)
#             adj_lst = adj(pos)
#             count = 0
#             if j == "-":
#                 for a in adj_lst:
#                     if grid[a[0]][a[1]] == "#":
#                         count += 1
#                 grid[index_I][index_J] = str(count)

#     return grid


# sample_grid = [
#     ["-", "-", "-", "-", "-"],
#     ["-", "-", "-", "-", "-"],
#     ["-", "-", "#", "-", "-"],
#     ["-", "-", "-", "-", "-"],
#     ["-", "-", "-", "-", "-"],
# ]

# print(numgrid(sample_grid))

# -----------------------------------------------------------

# b1 = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]]


# def tic_tac_toe(board):

#     # Check horizontal
#     for i in board:
#         if i[0] == i[1] and i[0] == i[2]:
#             return i[0]

#     # Check vertical

#     for x in range(len(board)):
#         if board[0][x] == board[1][x] and board[0][x] == board[2][x]:
#             return board[0][x]

#     # Check diagonals

#     if board[1][1] == board[0][0] and board[1][1] == board[2][2]:
#         return board[1][1]

#     if board[1][1] == board[2][0] and board[1][1] == board[0][2]:
#         return board[1][1]

#     return "Draw"


# print(tic_tac_toe(b1))


# ---------------------------------------------------------


# def deepest(arr):
#     res = 0
#     lst = arr

#     while True:
#         sublist = []
#         res += 1
#         for i in lst:
#             if type(i) == list:
#                 for x in i:
#                     sublist.append(x)
#         lst = sublist
#         if len(sublist) == 0:
#             return res


# print(deepest([1, [2, 3], 4, [5, 6]]))

# print(deepest([1, 3, 4, 5]))

# # Better way
# def deepest(lst):
#     	if type(lst)!= list: return 0
# 	return 1 + max(deepest(e) for e in lst)

# -------------------------------------------------------------


# def will_hit(equation, pos):
#     x, y = pos
#     eqn = equation.replace("=", "==").replace("x", "*x")
#     print(eqn)
#     return eval(eqn)


# print((will_hit("y = 2x - 5", (0, 0))))
# print((will_hit("y = -4x + 6", (1, 2))))
# print((will_hit("y = 2x + 6", (3, 2))))

# -------------------------------------------------------------


# maze1 = [
#     [0, 1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 1, 0, 1, 1],
#     [1, 0, 0, 0, 0, 1, 1],
#     [1, 1, 1, 1, 0, 0, 1],
#     [1, 1, 1, 1, 1, 0, 0],
# ]


# def canExit(maze):
#     start = (0, 0)
#     visitedNodes = []

#     def adj(node):
#         adjLst = []
#         transformations = [
#             (-1, 0),
#             (0, 1),
#             (0, -1),
#             (1, 0),
#         ]

#         for i in transformations:
#             trans = tuple(map(lambda y, x: x + y, node, i))
#             if (
#                 trans[1] >= 0
#                 and trans[1] < len(maze)
#                 and trans[0] >= 0
#                 and trans[0] < len(maze[0])
#                 and maze[trans[1]][trans[0]] == 0
#                 and trans not in visitedNodes
#             ):
#                 adjLst.append(trans)

#         return adjLst

#     def dfs(currentNode):
#         adjList = adj(currentNode)

#         if currentNode == (len(maze[0]) - 1, len(maze) - 1):
#             return True

#         if len(adjList) == 0:
#             return
#         else:
#             for x in adjList:
#                 visitedNodes.append(currentNode)
#                 # If you do 'return dfs(x)' it will recursively return none when it hits a len(adjList == 0), we need it to continue the loop in order to continue searching the path.
#                 if dfs(x):
#                     return True

#         return False

#     return dfs(start)


# print(canExit(maze1))

# -------------------------------------------------------------------------------------


# def guess_score(code, guess):
#     black = 0
#     white = 0
#     c = code

#     for i in range(len(c)):
#         if code[i] == guess[i]:
#             c = c.replace(guess[i], "", 1)
#             black += 1

#     for x in guess:
#         for index_k, k in enumerate(c):
#             if x == k:
#                 white += 1
#         c = c.replace(x, "", 1)

#     return {"black": black, "white": white}


# print(
#     guess_score("1423", "5678"),
#     guess_score("1423", "2222"),
#     guess_score("1423", "1234"),
#     guess_score("1423", "2211"),
#     guess_score("2928", "7722"),
# )


# --------------------------------------------------------------------------------------


# def priority_sort(lst, s):
#     return sorted(sorted(lst), key=lambda num: float("-inf") if num in s else num)


# def priority_sort(lst, s):
#     return sorted(lst, key=lambda x: (not x in s, x))


# print(priority_sort([1, 3, 2, -4, 7, -2, 6], [2, 3]))
# print(priority_sort([5, 4, 3, 2, 1], {2, 3}))

# x = [1, 2, 3, 4]
# a = 1

# print(not a in x)

# ------------------------------------------------------------------------------------


# def kaprekar(lower, upper):

#     res = []

#     for i in range(lower, upper + 1):
#         l = (
#             0
#             if str(i ** 2)[0 : len(str(i ** 2)) - len(str(i))] == ""
#             else int(str(i ** 2)[0 : len(str(i ** 2)) - len(str(i))])
#         )

#         r = int(str(i ** 2)[len(str(i ** 2)) - len(str(i)) :])
#         if l + r == i:
#             res.append(str(i))

#     if not res:
#         return "INVALID RANGE"
#     else:
#         return " ".join(res)


# print(kaprekar(1, 10))
# print(kaprekar(100, 300))
# print(kaprekar(2, 4))
# 100 => 10000 l = remaining r = 2 digits

# -------------------------------------------------------------


# def discount(lst):

#     import math

#     total_free_items = sum(sorted(lst)[0 : math.floor(len(lst) / 3)])
#     percentage = (100 - (100 * total_free_items) / sum(lst)) / 100

#     res = []

#     for i in lst:
#         res.append(round((i * percentage), 2))
#     return res


# print(discount([2.99, 5.75, 3.35, 4.99]))

# -------------------------------------------------------------


# def validateCard(card):

#     cardNums = []

#     if len(str(card)) < 14 or len(str(card)) > 19:
#         return False

#     for i, v in enumerate(list(str(card)[0 : len(str(card)) - 1])[::-1]):
#         if i % 2 == 0 or i == 0:
#             x = int(v) * 2
#             if len(str(x)) == 2:
#                 q = int(str(x)[0]) + int(str(x)[1])
#                 cardNums.append(q)
#                 continue
#             else:
#                 cardNums.append(x)
#                 continue
#         cardNums.append(int(v))

#     if 10 - int(str(sum(cardNums))[1]) == int(str(card)[len(str(card)) - 1]):
#         return True
#     else:
#         return False


# print(validateCard(709092739800713))

# --------------------------------------------------------------------------


# def shuffle(num):

#     nums = tuple([i for i in range(num)])

#     res = [i for i in range(num)]

#     count = 0
#     while True:
#         count += 1
#         sub = []
#         n1 = res[0 : int(num / 2)]
#         n2 = res[int(num / 2) :]
#         for x in range(int(num / 2)):
#             sub.append(n1[x])
#             sub.append(n2[x])
#         res = sub
#         if tuple(res) == nums:
#             return count


# print(shuffle(14))


# ----------------------------------------------------------------------


# def sort_records(csv_filename, new_filename):
#     f = open("./" + csv_filename)
#     r = f.read()
#     test = r.split(",")
#     row = r.split("\n")
#     sort = sorted(row[1:], key=lambda char: char[0])
#     result = " \n".join(row[:1] + sort)

#     writeFile = open("./" + new_filename, "w")
#     writeFile.write(result)
#     writeFile.close()
#     f.close()


# sort_records("max_temp.csv", "sorted.csv")

# import csv


# def sort_records(csv_filename, new_filename):
#     with open("./" + csv_filename) as csvfile:
#         content = csv.reader(csvfile, delimiter=",")
#         table = [i for i in content]
#         sort = [table[0]] + sorted(table[1:], key=lambda row: row[0][0])
#         print(sort)

#         with open("./" + new_filename, "w", encoding="UTF8", newline="") as writeFile:
#             writer = csv.writer(writeFile)
#             for i in sort:
#                 print(i)
#                 writer.writerow(i)


# sort_records("max_temp.csv", "hello.csv")

# -------------------------------------------------------------------------------------

# import csv
# import math


# def hottest_cities(csv_filename):
#     with open("./" + csv_filename) as csvfile:
#         content = csv.reader(csvfile, delimiter=",")
#         cities = [i for i in content][1:]

#         highest_temp = 0
#         highest_temp_cities = []

#         for x in cities:
#             val = round(
#                 float(sorted(x[1:], key=lambda num: float(num), reverse=True)[0]), 1
#             )
#             if val == highest_temp:
#                 highest_temp_cities.append(x[0])
#             elif val > highest_temp:
#                 highest_temp = val
#                 highest_temp_cities = [x[0]]

#         return highest_temp, sorted(highest_temp_cities)


# print(hottest_cities("max_temp.csv"))
# print(float(100.00) == float("00100.00"))

# ------------------------------------------------------------------------------------------


# def execute2_lds(plan, start, capacity):

#     # Greedy Search
#     greedy_plan = []
#     node = start

#     while len(plan) > 0:
#         shortest = sorted(
#             plan,
#             key=lambda delivery: abs(node[0] - delivery[1][0])
#             + abs(node[1] - delivery[1][1]),
#         )[0]

#         greedy_plan.append(shortest)
#         node = shortest[2]
#         plan.remove(shortest)

#     total_distance = 0

#     for subplan in greedy_plan:
#         delivery_qty = subplan[0]
#         distance1 = abs(start[0] - subplan[1][0]) + abs(start[1] - subplan[1][1])

#         distance2 = abs(subplan[1][0] - subplan[2][0]) + abs(
#             subplan[1][1] - subplan[2][1]
#         )

#         total_distance += distance1 + distance2
#         start = subplan[2]

#         while delivery_qty > capacity:
#             total_distance += 2 * distance2
#             delivery_qty -= capacity

#     return total_distance


# ----------------------------------------------------------------------------


# from itertools import permutations


# def execute2_lds(plan, start, capacity):

#     # Exhaustive Search
#     exhaustive_plan = [[x for x in i] for i in permutations(plan)]

#     shortest_distance = 0

#     for perm in exhaustive_plan:

#         start_node = start

#         total_distance = 0

#         for subplan in perm:
#             delivery_qty = subplan[0]
#             distance1 = abs(start_node[0] - subplan[1][0]) + abs(
#                 start_node[1] - subplan[1][1]
#             )

#             distance2 = abs(subplan[1][0] - subplan[2][0]) + abs(
#                 subplan[1][1] - subplan[2][1]
#             )
#             total_distance += distance1 + distance2
#             start_node = subplan[2]

#             while delivery_qty > capacity:
#                 total_distance += 2 * distance2
#                 delivery_qty -= capacity

#         if total_distance < shortest_distance or shortest_distance == 0:

#             shortest_distance = total_distance

#     return shortest_distance


# print(execute2_lds([(3, (1, 0), (3, 2)), (7, (2, 1), (0, 0))], (3, 3), 9))

# print(
#     execute2_lds(
#         [(8, (0, 0), (1, 4)), (2, (1, 0), (1, 4)), (4, (0, 0), (1, 0))], (0, 0), 5
#     )
# )
# print(execute2_lds([(3, (1, 0), (3, 2)), (7, (2, 1), (0, 0))], (0, 0), 9))
# print(execute2_lds([(3, (1, 0), (3, 2)), (7, (2, 1), (0, 0))], (3, 3), 9))

# print(
#     execute2_lds(
#         [(8, (0, 0), (1, 4)), (2, (1, 0), (1, 4)), (4, (0, 0), (1, 0))], (0, 0), 5
#     )
# )

# 10 + 5 + 1 + 4

# ---------------------------------------------------------------------------------

# import re

# lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]

# pattern = "(?<!good )cookie"

# print(len(re.findall(pattern, ", ".join(lst))))

# -------------------------------------------------------------------------------------

# s1 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
# s2 = [0, 0, 0, 0]

# import math


# def maximumSeating(lst):

#     for i, val in enumerate(lst):
#         if val == 0:
#             isValid = True
#             for x in range(i - 2, i + 3):
#                 if x != i and x >= 0 and x < len(lst):
#                     if lst[x] != 0:
#                         isValid = False
#                         break
#             if isValid:
#                 lst[i] = 2
#     return lst.count(2)


# print(maximumSeating(s1))

# --------------------------------------------------------------------------------------


# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution(object):
#     def mergeTwoLists(self, l1, l2):

#         listAll = []

#         node = l1
#         node2 = l2
#         while l1 != None:
#             listAll.append(node.val)
#             if node.next == None:
#                 break
#             else:
#                 node = node.next

#         while l2 != None:
#             listAll.append(node2.val)
#             if node2.next == None:
#                 break
#             else:
#                 node2 = node2.next

#         sorted_list = sorted(listAll)

#         list_final = res_list = ListNode()

#         for i in sorted_list:
#             res_list.next = ListNode(i)
#             res_list = res_list.next

#         return list_final.next


# n4 = ListNode(7)
# n3 = ListNode(5, n4)
# n2 = ListNode(3, n3)
# n1 = ListNode(2, n2)

# m4 = ListNode(9)
# m3 = ListNode(3, m4)
# m2 = ListNode(2, m3)
# m1 = ListNode(1, m2)

# result = Solution()

# print(result.mergeTwoLists(ListNode(), ListNode()))


# ------------------------------------------------------------------------

# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution(object):
#     def countNodes(self, root):

#         self.count = 0

#         def recursion(main):
#             node = main
#             self.count += 1
#             if node.left == None:
#                 return
#             else:
#                 for i in [node.left, node.right]:
#                     if i != None:
#                         recursion(i)

#         if root != None:
#             recursion(root)

#         return self.count


# s = TreeNode(
#     1,
#     TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)),
#     TreeNode(3, TreeNode(6, None, None), None),
# )

# a = Solution()

# print(a.countNodes(s))

# ---------------------------------------------------------------------------


# def tidy_link(url, name, hover=""):
#     n1 = "[%s]" % (name,)

#     n2 = "(%s " '"%s"' ")" % (url, hover) if hover != "" else "(%s)" % (url,)

#     return n1 + n2


# print(
#     tidy_link("https://www.google.com", "Google", "Google Search"),
# )

# ---------------------------------------------------------------------------


# def awardPrizes(n):

#     a = sorted(n, key=lambda item: n[item], reverse=True)

#     for index, value in enumerate(a):
#         if index == 0:
#             n[value] = "Gold"
#         elif index == 1:
#             n[value] = "Silver"
#         elif index == 2:
#             n[value] = "Bronze"
#         else:
#             n[value] = "Participation"

#     return n


# awardPrizes(
#     {"Person A": 1, "Person B": 2, "Person C": 3, "Person D": 4, "Person E": 102}
# )

# awardPrizes({"Mario": 99, "Luigi": 100, "Yoshi": 299, "Toad": 2})

# ------------------------------------------------------------------------


# def is_valid(str):

#     from collections import Counter

#     frequency = [x for x in Counter([char for char in str]).values()]

#     unique = list(set(frequency))

#     for i in unique:
#         if frequency.count(i) < len(frequency) - 1 and frequency.count(i) != 1:
#             return "NO"

#     if len(unique) == 2:
#         if abs(unique[0] - unique[1]) != 1:
#             return "NO"

#     return "YES"


# print(is_valid("abcdefghhgfedecba"))

# --------------------------------------------------------------------


# def canCompleteCircuit(gas, cost):

#     for start in range(len(gas)):
#         tank = 0
#         i = start
#         while i < len(gas):
#             tank += gas[i]
#             tank -= cost[i]
#             if tank < 0:
#                 break
#             i += 1

#             if i == start:
#                 return start

#             if i >= len(gas):
#                 i = 0

#             if start == 0 and i == 0:
#                 return start

#     return -1


# g1 = [1, 2, 3, 4, 5]
# c1 = [3, 4, 5, 1, 2]

# g2 = [2, 3, 4]
# c2 = [3, 4, 3]
# print(canCompleteCircuit(g2, c2))


# def canCompleteCircuit(gas, cost):

#     tank = 0
#     count = 0
#     index = 0
#     for i in range(len(gas)):

#         tank += gas[i] - cost[i]

#         if tank < 0:
#             index = i + 1
#             count += tank
#             tank = 0

#         if i == len(gas) - 1:
#             if tank + count >= 0:
#                 return index
#             else:
#                 return -1


# g1 = [1, 2, 3, 4, 5]
# c1 = [3, 4, 5, 1, 2]

# g2 = [2, 3, 4]
# c2 = [3, 4, 3]

# g3 = [4, 5, 2, 6, 5, 3]
# c3 = [3, 2, 7, 3, 2, 9]
# print(canCompleteCircuit(g2, c2))

# -------------------------------------------------------

# INORDER TRAVERSIAL - provides the correct order


# def isValidBST(root):

#     inorder = []

#     def inorder_traversial(r, inorder):
#         if r:
#             inorder_traversial(r.left, inorder)
#             inorder.append(r.val)
#             inorder_traversial(r.right, inorder)

#     inorder_traversial(root, inorder)

#     return sorted(inorder) == inorder and len(inorder) == len(set(inorder))


# # --------------------------------------------------------


# def bingo_check(board):

#     # Check horizontals
#     for i in board:
#         h = True
#         for x in i:
#             if x != "x":
#                 h = False
#                 break
#         if h == True:
#             return True

#     # Check verticals
#     for x in range(len(board[0])):
#         v = True
#         for k in board:
#             if k[x] != "x":
#                 v = False
#                 break
#         if v == True:
#             return True

#     for m in range(len(board)):
#         if board[m][m] != "x":
#             break
#         return True

#     s = 0
#     d = True
#     for l in range(len(board) - 1, 0, -1):
#         if board[s][l] != "x":
#             d = False
#             break
#         s += 1
#     return d


# print(
#     bingo_check(
#         [
#             ["x", 43, 31, 74, 87],
#             [64, "x", 47, 32, 90],
#             [37, 65, "x", 83, 54],
#             [67, 98, 39, "x", 44],
#             [21, 59, 24, 30, "x"],
#         ]
#     )
# )

# print(
#     bingo_check(
#         [
#             [45, "x", 31, 74, 87],
#             [64, 78, 47, "x", 90],
#             [37, "x", 68, 83, 54],
#             [67, "x", 98, "x", 44],
#             [21, "x", 24, 30, 52],
#         ]
#     )
# )

# -------------------------------------------------------------------------

# Please don't modify the code below the traverse function is in BST class

# # Node class
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# # BST Class
# class BST:
#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#         else:
#             current = self.head
#             while True:
#                 if data > current.data and current.right:
#                     current = current.right
#                 elif data < current.data and current.left:
#                     current = current.left
#                 elif data > current.data:
#                     current.right = new_node
#                     break
#                 else:
#                     current.left = new_node
#                     break
#         return self.head

#     def traverse(self):
#         # Complete the code here
#         res = []

#         to_visit = [self.head]

#         current_node = self.head

#         while current_node:

#             if current_node.left:
#                 to_visit.append(current_node.left)

#             if current_node.right:
#                 to_visit.append(current_node.right)

#             res.append(to_visit[0].data)
#             to_visit.pop(0)
#             if not to_visit:
#                 break
#             current_node = to_visit[0]
#         return res


# b = BST()
# b.insert(100)
# b.insert(200)
# b.insert(70)
# b.insert(34)
# b.insert(80)
# b.insert(85)
# b.insert(85)
# b.insert(111)

# print(b.traverse())


# ---------------------------------------------------------------------------------------


# def can_see_stage(seats):

#     for i in range(len(seats[0])):

#         col = []

#         for j in range(len(seats)):

#             col.append(seats[j][i])

#         if sorted(col) != col or len(set(col)) != len(col):
#             return False

#     return True


# print(can_see_stage([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# --------------------------------------------------------------------------------------


# def show_the_love(lst):

#     count = 0
#     lowest = lst.index(sorted(lst)[0])

#     for i in range(len(lst)):
#         if lst[i] != sorted(lst)[0]:
#             count += lst[i] * 0.25
#             lst[i] -= lst[i] * 0.25

#     lst[lowest] += count

#     return lst


# print(show_the_love([16, 10, 8]))
# print(show_the_love([54, 62, 59]))


# -------------------------------------------------------------------------------------

# Memoisation


# def wordbreak(s, wordDict):
#     dp = [False] * (len(s) + 1)
#     dp[len(s)] = True

#     for i in range(len(s) - 1, -1, -1):
#         for w in wordDict:
#             if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
#                 dp[i] = dp[i + len(w)]
#             if dp[i]:
#                 break

#     return dp[0]

# ------------------------------------------------------------------------------------


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def removeNthNode(head, n):

#     nodes = []

#     node = head

#     while True:

#         if node == None:
#             break

#         nodes.append(node)

#         node = node.next

#     if nodes[len(nodes) - n] != head:
#         nodes[len(nodes) - n - 1].next = nodes[len(nodes) - n].next
#         return head
#     else:
#         return head.next


# n5 = ListNode(5, None)
# n4 = ListNode(4, n5)
# n3 = ListNode(3, n4)
# n2 = ListNode(2, n3)
# n1 = ListNode(1, n2)

# # removeNthNode(n1, 2)

# m = n1
# while True:
#     if m == None:
#         break
#     print(m.val)
#     m = m.next


# -------------------------------------------------------


# def swapPairs(head):

#     if head == None:
#         return

#     if head.next == None:
#         return head

#     nextNode = head.next.next

#     transNode = head.next

#     head.next.next = head

#     head.next = swapPairs(nextNode)

#     return transNode


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# n5 = ListNode(5, None)
# n4 = ListNode(4, n5)
# n3 = ListNode(3, n4)
# n2 = ListNode(2, n3)
# n1 = ListNode(1, n2)

# swapPairs(n1)

# m = n2
# while True:
#     if m == None:
#         break
#     print(m.val)
#     m = m.next

# ---------------------------------------------------------------


# def replace_chars(word, k):

#     chars = "abcdefghijklmnopqrstuvwxyz"

#     res = ""

#     for i in range(len(word)):
#         if i >= k - 1:
#             index = chars.index(word[i])
#             res += chars[len(chars) - index - 1]
#         else:
#             res += word[i]

#     return res


# print(replace_chars("smiley", 1))
# print(replace_chars("hello", 1))
# print(replace_chars("playground", 1))
# print(replace_chars("paint", 3))
# print(replace_chars("computer", 9))


# ---------------------------------------------------


# def assign_colours(message, lower_cols_list, upper_cols_list):

#     res = []

#     lowerCount = 0
#     upperCount = 0
#     for i in message:
#         subres = []
#         if i == " ":
#             subres = [" ", None]
#         elif i.isalpha() == False:
#             subres = [i, "Silver"]
#         elif i.isupper():
#             subres = [i, upper_cols_list[upperCount % len(upper_cols_list)]]
#             upperCount += 1
#         else:
#             subres = [i, lower_cols_list[lowerCount % len(lower_cols_list)]]
#             lowerCount += 1

#         res.append(subres)

#     return res


# print(assign_colours("A cat hat", ["red", "green", "blue"], ["yellow"]))
# print(
#     assign_colours(
#         "Congrats on Graduation!", ["blue", "turquoise", "black"], ["yellow"]
#     )
# )
# print(
#     assign_colours(
#         "?We are having twins?",
#         ["purple", "black"],
#         ["red", "orange", "yellow", "green", "blue"],
#     )
# )

# -----------------------------------------------------------


# def switcheroo(str):
#     import re

#     res = []

#     for i in str.split(" "):
#         if bool(re.search("nce(?!\w)", i)):
#             res.append(re.sub("nce(?!\w)", "nts", i))
#             continue
#         if bool(re.search("nts(?!\w)", i)):
#             res.append(re.sub("nts(?!\w)", "nce", i))
#             continue
#         res.append(i)
#     return " ".join(res)


# print(switcheroo("While he rants, I fall into ance trance..."))


# --------------------------------------------------------------


# def identify(*cube):

#     cube_list = [len(i) for i in cube]
#     maximum = max(cube_list)
#     count = 0
#     for i in cube_list:
#         count += maximum - i

#     if count > 0:
#         return "Missing {}".format(count)
#     elif len(cube_list) != maximum:
#         return "Non-Full"
#     else:
#         return "Full"


# print(identify(["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]))
# print(identify(["O", "O", "O"], ["O", "O", "O"]))


# --------------------------------------------------------------


# def isRobotBounded(instructions):

#     orientation = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     pos = (0, 0)
#     index = 0

#     for i in instructions:
#         direction = orientation[index % len(orientation)]
#         if i == "G":
#             pos = tuple(map(lambda k, j: k + j, direction, pos))
#         elif i == "R":
#             index += 1
#         else:
#             index -= 1

#     if index % len(orientation) != 0 or pos == (0, 0):
#         return True
#     return False


# print(isRobotBounded("GLGLGGLGL"))

# -----------------------------------------------------------------

# non-capturing groups essentially mean that we do not want the items in the non-capture group to be present by themselves int he resulting output

# import re


# def nonCapture(str):

#     pattern = "(?<=\W)(?:an|a|the)(?! an | a | the ) (?:\w+)"
#     pattern2 = r"(?:\ban\b|\ba\b|\bthe\b)(?! an | a | the ) (?:\w+)"
#     # Need to use prefix "r" on pattern2 as regex will interpret the \b as a backspace character - note the different colouring. Using "r" as a prefix on the string makes it interpret it as a raw string. You can see the same thing happening with the "+" symbol

#     return re.findall(pattern2, str)


# print(nonCapture("the chick the Italian and she is French an this"))

# ------------------------------------------------------------------


# def sudoku_validator(bo):

#     # Check horiztonal
#     for i in bo:
#         if len(set(i)) != 9:
#             return False

#     # Check certical
#     for i in range(len(bo)):
#         check = []
#         for j in range(len(bo[i])):
#             check.append(bo[j][i])
#         if len(set(check)) != 9:
#             return False

#     # Check box
#     box1 = []
#     box2 = []
#     box3 = []
#     for i in range(len(bo)):
#         for x in range(len(bo[i])):
#             if x // 3 == 0:
#                 box1.append(bo[i][x])
#             if x // 3 == 1:
#                 box2.append(bo[i][x])
#             if x // 3 == 2:
#                 box3.append(bo[i][x])

#         if (i + 1) % 3 == 0:
#             if len(set(box1)) != 9 or len(set(box2)) != 9 or len(set(box2)) != 9:
#                 return False
#             box1 = []
#             box2 = []
#             box3 = []

#     return True


# bo1 = [
#     [1, 5, 2, 4, 8, 9, 3, 7, 6],
#     [7, 3, 9, 2, 5, 6, 8, 4, 1],
#     [4, 6, 8, 3, 7, 1, 2, 9, 5],
#     [3, 8, 7, 1, 2, 4, 6, 5, 9],
#     [5, 9, 1, 7, 6, 3, 4, 2, 8],
#     [2, 4, 6, 8, 9, 5, 7, 1, 3],
#     [9, 1, 4, 6, 3, 7, 5, 8, 2],
#     [6, 2, 5, 9, 4, 8, 1, 3, 7],
#     [8, 7, 3, 5, 1, 2, 9, 6, 4],
# ]

# bo2 = [
#     [1, 1, 2, 4, 8, 9, 3, 7, 6],
#     [7, 3, 9, 2, 5, 6, 8, 4, 1],
#     [4, 6, 8, 3, 7, 1, 2, 9, 5],
#     [3, 8, 7, 1, 2, 4, 6, 5, 9],
#     [5, 9, 1, 7, 6, 3, 4, 2, 8],
#     [2, 4, 6, 8, 9, 5, 7, 1, 3],
#     [9, 1, 4, 6, 3, 7, 5, 8, 2],
#     [6, 2, 5, 9, 4, 8, 1, 3, 7],
#     [8, 7, 3, 5, 1, 2, 9, 6, 4],
# ]

# bo3 = [
#     [1, 5, 2, 4, 8, 9, 3, 7, 6],
#     [7, 3, 9, 2, 5, 6, 8, 4, 1],
#     [4, 6, 5, 3, 7, 1, 2, 9, 8],
#     [3, 8, 7, 1, 2, 4, 6, 5, 9],
#     [8, 9, 1, 7, 6, 3, 4, 2, 5],
#     [2, 4, 6, 5, 9, 8, 7, 1, 3],
#     [9, 1, 4, 6, 3, 7, 5, 8, 2],
#     [6, 2, 8, 9, 4, 5, 1, 3, 7],
#     [5, 7, 3, 8, 1, 2, 9, 6, 4],
# ]

# bo4 = [
#     [2, 5, 1, 4, 6, 9, 3, 7, 8],
#     [7, 8, 9, 2, 1, 3, 4, 5, 6],
#     [4, 3, 6, 5, 8, 7, 2, 9, 1],
#     [6, 1, 3, 8, 7, 2, 5, 4, 9],
#     [9, 7, 4, 1, 5, 6, 8, 2, 3],
#     [8, 2, 5, 9, 3, 4, 1, 6, 7],
#     [5, 6, 7, 3, 4, 8, 9, 1, 2],
#     [2, 4, 8, 6, 9, 1, 7, 3, 5],
#     [3, 9, 1, 7, 2, 5, 6, 8, 4],
# ]
# print(sudoku_validator(bo4))


# -----------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# def inorder(root):

#     lst = []

#     def traversal(r, lst):
#         if r:
#             traversal(r.left, lst)
#             lst.append(r)
#             traversal(r.right, lst)
#         else:
#             return

#     traversal(root, lst)

#     return lst


# n3 = TreeNode(3, None, None)
# n2 = TreeNode(2, n3, None)
# n1 = TreeNode(1, None, n2)

# print(inorder(n1))


# ------------------------------------------------

# leetCode Valid Parenthese
# def isValid(s):

#     if len(s) == 0:
#         return True

#     n = {"(": ")", "{": "}", "[": "]", ")": "", "}": "", "]": ""}

#     for i in range(len(s) - 1, 0, -1):
#         if n[s[0]] == s[i]:
#             if isValid(s[1:i]) and isValid(s[i + 1 :]):
#                 return True

#     return False


# print(isValid("(()())())"))


# -----------------------------------------------


#  3SumClosest - leetcode


# def threeSumClosest(nums, target):

#     sort = sorted(nums)
#     res = float("inf")
#     subres = 0
#     for i in range(len(nums) - 1):

#         left = i + 1
#         right = len(sort) - 1

#         count = float("inf")
#         while left < right:

#             numSum = sort[i] + sort[left] + sort[right]

#             if numSum == target:
#                 return numSum

#             if numSum > target:
#                 right -= 1
#             elif numSum < target:
#                 left += 1

#             if abs(numSum - target) < count:
#                 count = abs(numSum - target)
#                 subres = numSum

#         if abs(subres - target) < abs(res - target):
#             res = subres

#     return res


# print(threeSumClosest([0, 1, 2], 0))
# -4, -1, 1. 2

# -------------------------------------------------------

#  Fives and Threes Only - edabit


# def only5and3(num):

#     if num == 5 or num == 3:
#         return True

#     if num < 1:
#         return False

#     if only5and3(num - 5) or only5and3(num / 3):
#         return True
#     else:
#         return False


# print(only5and3(25))


# -----------------------------------------------------


# Imaginary Coding Interview - edabit


# def interview(lst, tot):

#     if tot > 120 or len(lst) != 8:
#         return "disqualified"

#     difficulty = [
#         "very easy",
#         "very easy",
#         "easy",
#         "easy",
#         "medium",
#         "medium",
#         "hard",
#         "hard",
#     ]

#     for i, v in enumerate(lst):
#         if (
#             (difficulty[i] == "very easy" and v > 5)
#             or (difficulty[i] == "easy" and v > 10)
#             or (difficulty[i] == "medium" and v > 15)
#             or (difficulty[i] == "hard" and v > 20)
#         ):
#             return "disqualified"

#     return "qualified"


# print(
#     interview([5, 5, 10, 10, 15, 15, 20, 20], 120),
#     interview([5, 5, 10, 10, 25, 15, 20, 20], 120),
# )

# ------------------------------------------------------------

# Roman to Interger - leetcode


# def romanToInt(s):

#     res = 0

#     romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

#     for i in range(len(s) - 1, -1, -1):

#         if i < len(s) - 1 and list(romanDict).index(s[i]) < list(romanDict).index(
#             s[i + 1]
#         ):
#             res -= romanDict[s[i]]
#         else:
#             res += romanDict[s[i]]

#     return res


# print(romanToInt("XIV"), romanToInt("LVIII"))


# --------------------------------------------------------------

# Majority Element - leetcode


# def majorityElement(nums):

#     hashTable = {}

#     for i in nums:

#         if i in hashTable:
#             hashTable[i] += 1
#         else:
#             hashTable[i] = 1

#     return sorted(hashTable, key=lambda x: hashTable[x], reverse=True)[0]


# print(majorityElement([3, 3, 3, 2, 2, 2, 2, 1]))

# --------------------------------------------------------------

#  Count Animals - edabit

# Goal is to find the deepest point of the tree (non-binary)


# def count_animals(txt):

#     animals = [
#         "dog",
#         "cat",
#         "bat",
#         "cock",
#         "cow",
#         "pig",
#         "fox",
#         "ant",
#         "bird",
#         "lion",
#         "wolf",
#         "deer",
#         "bear",
#         "frog",
#         "hen",
#         "mole",
#         "duck",
#         "goat",
#     ]

#     res = []

#     def recursion(text, count=0):

#         for i in animals:

#             newText = text

#             match = True

#             print(newText, i)

#             for x in i:
#                 if newText.find(x) != -1:
#                     newText = newText.replace(x, "", 1)
#                 else:
#                     match = False
#                     break

#             if match:
#                 recursion(newText, count + 1)

#         res.append(count)

#     recursion(txt)

#     return max(res)


# print(count_animals("goatcode"))

# ----------------------------------------------------------

# WordSearch - edabit


# def wordSearch(letters, words):

#     grid = [[rows for rows in letters][8 * i : 8 * i + 8] for i in range(8)]

#     horizontal = ["".join(row) for row in grid]

#     horizontalReverse = ["".join(reversed(row)) for row in grid]

#     vertical = ["".join(col) for col in [[row[i] for row in grid] for i in range(8)]]

#     verticalReverse = [
#         "".join(reversed(col)) for col in [[row[i] for row in grid] for i in range(8)]
#     ]

#     diagonalRight = [
#         "".join([grid[x][x - i] for x in range(i, 8)]) for i in range(8)
#     ] + ["".join([grid[x - i][x] for x in range(i, 8)]) for i in range(1, 8)]

#     diagonalRightMirror = [
#         "".join([grid[x][x - i] for x in range(7, i - 1, -1)]) for i in range(8)
#     ] + ["".join([grid[x - i][x] for x in range(7, i - 1, -1)]) for i in range(1, 8)]

#     diagonalLeft = [
#         "".join([grid[x][i - x] for x in range(i + 1)]) for i in range(7, -1, -1)
#     ] + ["".join([grid[i - x][x] for x in range(7, i, -1)]) for i in range(8)]

#     diagonalLeftMirror = [
#         "".join([grid[x][i - x] for x in range(i, -1, -1)]) for i in range(7, -1, -1)
#     ] + ["".join([grid[x][i - x] for x in range(7, i, -1)]) for i in range(8)]

#     for word in words:
#         match = False
#         for q in (
#             horizontalReverse
#             + horizontal
#             + vertical
#             + verticalReverse
#             + diagonalRight
#             + diagonalRightMirror
#             + diagonalLeft
#             + diagonalLeftMirror
#         ):

#             if word.upper() in q:
#                 match = True

#         if match == False:
#             return False

#     return True


# # 17, 16, 15, 14, 13

# l = "PSUWHATSLPACKAGENYOLRDVLFINGEZBMIREHQNJOATBVGYESJDUWUESTPSTICKEY"
# w = ["stick", "most", "key", "vein", "yes", "package", "tube", "target", "elm", "spy"]

# print(wordSearch(l, w))


# Word Search (Part 2) - edabit

# Quick solution - simply double each row, col and diagonals - For the word to wrap the word must appear within 2 passes of the row, col, diagonal etc.


# def wordSearch(letters, words):

#     grid = [[rows for rows in letters][8 * i : 8 * i + 8] for i in range(8)]

#     horizontal = ["".join(row) * 2 for row in grid]

#     horizontalReverse = ["".join(reversed(row)) * 2 for row in grid]

#     vertical = [
#         "".join(col) * 2 for col in [[row[i] for row in grid] for i in range(8)]
#     ]

#     verticalReverse = [
#         "".join(reversed(col)) * 2
#         for col in [[row[i] for row in grid] for i in range(8)]
#     ]

#     diagonalRight = [
#         "".join([grid[x][x - i] for x in range(i, 8)]) * 2 for i in range(8)
#     ] + ["".join([grid[x - i][x] for x in range(i, 8)]) * 2 for i in range(1, 8)]

#     diagonalRightMirror = [
#         "".join([grid[x][x - i] for x in range(7, i - 1, -1)]) * 2 for i in range(8)
#     ] + [
#         "".join([grid[x - i][x] for x in range(7, i - 1, -1)]) * 2 for i in range(1, 8)
#     ]

#     diagonalLeft = [
#         "".join([grid[x][i - x] for x in range(i + 1)]) * 2 for i in range(7, -1, -1)
#     ] + ["".join([grid[i - x][x] for x in range(7, i, -1)]) * 2 for i in range(8)]

#     diagonalLeftMirror = [
#         "".join([grid[x][i - x] for x in range(i, -1, -1)]) * 2
#         for i in range(7, -1, -1)
#     ] + ["".join([grid[x][i - x] for x in range(7, i, -1)]) * 2 for i in range(8)]

#     for word in words:
#         match = False
#         for q in (
#             horizontalReverse
#             + horizontal
#             + vertical
#             + verticalReverse
#             + diagonalRight
#             + diagonalRightMirror
#             + diagonalLeft
#             + diagonalLeftMirror
#         ):

#             if word.upper() in q:
#                 match = True

#         if match == False:
#             return False

#     return True


# l2 = "HWAVEOWCFONNANFABEOAMOIAHODOXORTACTIDINOBWZODGELINEEAFASTETAPELL"
# w2 = [
#     "slot",
#     "donate",
#     "orthodox",
#     "rated",
#     "wave",
#     "tape",
#     "leg",
#     "habit",
#     "add",
#     "fox",
# ]

# print(wordSearch(l2, w2))

# ----------------------------------------------------------------------

# 144. Binary Preorder Traversial - leetcode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# def preorder_traversial(root):

#     order = []

#     def preorder(r, order=[]):

#         if r:
#             order.append(r.val)
#             preorder(r.left, order)
#             preorder(r.right, order)

#     preorder(root, order)
#     return order


# n6 = TreeNode(6)
# n5 = TreeNode(5)
# n4 = TreeNode(4)
# n3 = TreeNode(3, n6)
# n2 = TreeNode(2, n4, n5)
# n1 = TreeNode(1, n2, n3)

# print(preorder_traversial(n1))


# -----------------------------------------------------

# Party People Part I: Make it Recursive - edabit


# def party_people(lst):

#     people = []

#     for i in lst:
#         if i <= len(lst):
#             people.append(i)

#     if len(lst) == len(people):
#         return len(people)

#     return party_people(people)


# print(party_people([4, 5, 4, 1]))

# ---------------------------------------------------


# Permutations - leetcode

# import itertools


# def permute(n):

#     res = []
#     for i in itertools.permutations(n):
#         res.append(list(i))

#     return res


# permute([1, 2, 3])

# ------------------------------------------------------------------------


# counter - edabit


# def counter():
#     if hasattr(counter, "count"):
#         counter.count += 1
#     else:
#         counter.count = 0

#     print(counter.count)


# counter()
# counter()
# counter()
# counter()

# -------------------------------------------------------------------------

# Manipulating Randomness - edabit


# def manipulate():

#     class s:
#         def __eq__(self, other):
#             return True

#     return s()

# --------------------------------------------------------------------------

# Piggy Bank - edabit


# def num_of_days(cost, savings, start):

#     target = cost - savings

#     sum = 0

#     current = start

#     days = 0

#     while sum < target:

#         if days != 0 and days % 7 == 0:
#             current -= 6

#         sum += current

#         current += 1

#         days += 1

#     return days


# print(num_of_days(10000, 2500, 50))

# ---------------------------------------------------------------

# Eight Sums Up - edabit


# def sums_up(lst):

#     res = {"pairs": []}

#     hashMap = {}

#     for i in lst:
#         if str(8 - i) in hashMap:
#             res["pairs"].append([min(8 - i, i), max(8 - i, i)])
#         else:
#             hashMap[str(i)] = 1
#     return res


# print(sums_up([1, 6, 5, 4, 8, 2, 3, 7]))

# ----------------------------------------------------------------

# Two Sum - leetcode


# def twoSum(nums, target):

#     hashMap = {}

#     for i, v in enumerate(nums):
#         print(str(target - v) in hashMap)
#         if str(target - v) in hashMap:
#             return [hashMap[str(target - v)], i]
#         else:
#             hashMap[str(v)] = i

#     return hashMap


# n = [2, 7, 11, 15]

# t = 9

# print(twoSum(n, t))


# ---------------------------------------------------------

# Linked List Cycle - leetcode


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def hasCycle(head):

#     # To account for head == none '[]'

#     if head == None:
#         return False

#     hashTable = {}

#     node = head

#     while True:

#         if node.next == None:
#             return False

#         if str(node.val) in hashTable:
#             hashTable[str(node.val)].append(node)
#         else:
#             hashTable[str(node.val)] = [node]

#         if (
#             str(node.next.val) in hashTable
#             and node.next in hashTable[str(node.next.val)]
#         ):
#             return True

#         node = node.next


# l1 = ListNode(1)


# print(hasCycle(l1))

# ------------------------------------------------------------------

# Linked List Cycle II - leetcode


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def hasCycle(head):

#     # To account for head == none '[]'

#     if head == None:
#         return

#     hashTable = {}

#     node = head

#     while True:

#         if node.next == None:
#             return

#         if str(node.val) in hashTable:
#             hashTable[str(node.val)].append(node)
#         else:
#             hashTable[str(node.val)] = [node]

#         if (
#             str(node.next.val) in hashTable
#             and node.next in hashTable[str(node.next.val)]
#         ):
#             return node.next

#         node = node.next


# l1 = ListNode(1)


# print(hasCycle(l1))


# ----------------------------------------------------------------------

# FizzBuzz - edabit


# def fizzBuzz(n):

#     if n % 3 == 0 and n % 5 == 0:
#         return "FizzBuzz"
#     if n % 3 == 0:
#         return "Fizz"
#     if n % 5 == 0:
#         return "Buzz"
#     return str(n)


# print(fizzBuzz(3))

# ----------------------------------------------------------------------

# Contact List - edabit


# def sort_contacts(names, sort):

#     if names == None or len(names) == 0:
#         return []

#     s = True if sort == "DESC" else False

#     return sorted(
#         names, key=lambda name: name.split(" ")[len(name.split(" ")) - 1], reverse=s
#     )


# print(sort_contacts(None, "ASC"))

# -----------------------------------------------------------------------

# Best Time to Buy and Sell Stock - leetcode


# def maxProfit(prices):

#     res = 0

#     for i, v in enumerate(prices):
#         if i < len(prices) - 1 and max(prices[i + 1 :]) - v > res:
#             res = max(prices[i + 1 :]) - v

#     return res


# print(maxProfit([7, 3, 4, 5, 1]))


# def maxProfit(prices):

#     maxProfit = 0
#     minPrice = float("inf")

#     for i in prices:
#         if i < minPrice:
#             minPrice = i
#         elif i - minPrice > maxProfit:
#             maxProfit = i - minPrice

#     return maxProfit


# print(maxProfit([7, 1, 5, 3, 6, 4]))

# --------------------------------------------------------

# Single Number - leetcode


# def singleNumber(nums):

#     hashMap = {}

#     for i in nums:
#         if str(i) in hashMap:
#             hashMap[str(i)] = True
#         else:
#             hashMap[str(i)] = False

#     for i in hashMap:
#         if hashMap[i] == False:
#             return int(i)


# print(singleNumber([4, 1, 2, 1, 2]))

# ---------------------------------------------------------

# Maximum Sum - edabit

# Kadane's Algorithm

# s1 = [10, -9, 0, -8, 76, 5, -40, 43]


# def maxSum(nums):
#     max_current = max_global = 0

#     for i in nums:
#         max_current = max(i, max_current + i)
#         if max_current > max_global:
#             max_global = max_current

#     return max_global


# print(maxSum(s1))

# -------------------------------------------------------------

# Path Sum - leetcode


# def hasPathSum(root, targetSum):

#     if root == None:
#         return False

#     def preorder(r, sum=0):

#         if r == None:
#             return False

#         newSum = sum + r.val

#         if r.left == None and r.right == None and newSum == targetSum:
#             return True

#         if r:
#             if preorder(r.left, newSum):
#                 return True
#             else:
#                 return preorder(r.right, newSum)

#         return False

#     return preorder(root)


# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# n7 = TreeNode(7)
# n2 = TreeNode(2)
# n11 = TreeNode(11, n7, n2)
# n4 = TreeNode(4, n11)
# n1 = TreeNode(1)
# n4r = TreeNode(4, None, n1)
# n13 = TreeNode(13)
# n8 = TreeNode(8, n13, n4r)
# n5 = TreeNode(5, n4, n8)

# print(hasPathSum(n5, 22))

# s2 = TreeNode(2)
# s3 = TreeNode(3)
# s1 = TreeNode(1, s2, s3)

# print(hasPathSum(s1, 5))

# ---------------------------------------------------------------

# Postman Harry - edabit


# def harry(matrix):

#     if len(matrix[0]) == 0:
#         return -1

#     res = []

#     def bfs(node, s=0):
#         if node == (len(matrix) - 1, len(matrix[len(matrix) - 1]) - 1):
#             res.append(s + matrix[node[0]][node[1]])
#             return

#         adj = []

#         if node[0] + 1 < len(matrix):
#             adj.append((node[0] + 1, node[1]))

#         if node[1] + 1 < len(matrix[len(matrix) - 1]):
#             adj.append((node[0], node[1] + 1))

#         for i in adj:
#             bfs(i, s + matrix[node[0]][node[1]])

#     bfs((0, 0))

#     return max(res)


# print(
#     harry(
#         [
#             [5, 6, 2, 5, 1],
#             [7, 2, 4, 1, 2],
#             [0, 7, 111, 2, 14],
#             [9, 5, 12, 5, 9],
#             [19, 5, 2, 6, 2],
#         ]
#     )
# )

# ----------------------------------------------------------------------


# Search a 2D Matrix - leetcode


# def searchMatrix(matrix, target):

#     start, end = 0, len(matrix) - 1

#     while start <= end:
#         mid = round((start + end) / 2)

#         if target in matrix[mid]:
#             return True

#         if target > max(matrix[mid]):
#             start = mid + 1
#         else:
#             end = mid - 1

#     return False


# print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 34))

# ------------------------------------------------------------------------


# Ordering People in Line - edabit


# def order_people(space, nums):

#     if space[0] * space[1] < nums:
#         return "overcrowded"

#     res = []

#     x = 1

#     for i in range(space[0]):

#         s = []

#         for j in range(space[1]):

#             if x <= nums:
#                 if i == 0 or i % 2 == 0:
#                     s.append(x)
#                 else:
#                     s.insert(0, x)
#             else:
#                 if i == 0 or i % 2 == 0:
#                     s.append(0)
#                 else:
#                     s.insert(0, 0)
#             x += 1

#         res.append(s)

#     return res


# print(order_people([4, 3], 5))

# -------------------------------------------------------

# Up the Hill, Down the Hill - edabit


# def ave_spd(u_time, u_rate, d_rate):

#     total_distance = (u_time / 60 * u_rate) * 2

#     total_time = u_time / 60 + (u_time / 60 * u_rate) / d_rate

#     return round(total_distance / total_time)


# print(ave_spd(18, 20, 60))

# ---------------------------------------------------------

# Smiley Faces - edabit


# def happinessNumber(s):

#     count = 0

#     for i in range(len(s)):
#         if i > 0:
#             if s[i] == "(" and s[i - 1] == ":":
#                 count -= 1
#             if s[i] == ")" and s[i - 1] == ":":
#                 count += 1
#             if s[i] == ":" and s[i - 1] == "(":
#                 count += 1
#             if s[i] == ":" and s[i - 1] == ")":
#                 count -= 1
#     return count


# print(happinessNumber(":):("))

# ----------------------------------------------------------

# Intersecting Rows and Columns - edabit


# def transform_matrix(m):

#     res = [[0 for i in x] for x in m]

#     for i, val in enumerate(m):

#         for j, val2 in enumerate(val):

#             count = val.count(1) - 1 if m[i][j] == 1 else val.count(1)

#             for x in range(len(m)):
#                 if m[x][j] == 1 and x != i:
#                     count += 1

#             res[i][j] = count

#     return res


# print(transform_matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

# -------------------------------------------------

# Block Dude - edabit


# def can_traverse(stairs):

#     prev_count = 0

#     for i in range(len(stairs[0])):

#         count = 0

#         for j in range(len(stairs)):

#             if stairs[j][i] == 1:
#                 count += 1

#         if abs(count - prev_count) > 1:
#             return False

#         prev_count = count

#     return True


# print(
#     can_traverse(
#         [
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0, 0, 1],
#             [0, 0, 1, 1, 1, 0, 1, 1, 1],
#             [0, 1, 1, 1, 1, 1, 1, 1, 1],
#         ]
#     )
# )

# ---------------------------------------------------------------------

# Valid Palindrome - leetcode


# def isPalindrome(s):

#     import re

#     s1 = re.sub("[^a-z0-9]", "", s.lower())

#     left = 0
#     right = len(s1) - 1

#     while left <= right:
#         if s1[left] != s1[right]:
#             return False

#         left += 1

#         right -= 1
#     return True


# print(isPalindrome("A man, a plan, a canal: Panama"))

# -----------------------------------------------------------------

# Two Product Problem - edabit


# def twoProduct(arr, target):

#     hashMap = {}

#     for count, i in enumerate(arr):
#         print(hashMap)
#         if target / i in hashMap:
#             return [int(target / i), i]
#         else:
#             hashMap[i] = count

# ----------------------------------------------------------------

# Minimum Path Sum - leetcode


# def minPathSum(grid):

#     count = []

#     def bfs(n, s=0):

#         newSum = grid[n[0]][n[1]] + s

#         if n == (len(grid) - 1, len(grid[0]) - 1):
#             count.append(newSum)

#         if n[0] + 1 < len(grid):
#             bfs((n[0] + 1, n[1]), newSum)

#         if n[1] + 1 < len(grid[0]):
#             bfs((n[0], n[1] + 1), newSum)

#     bfs((0, 0))

#     return min(count)


# g = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

# print(minPathSum(g))


# def minPathSum(grid):

#     if len(grid) == 0 or len(grid[0]) == 0:
#         return 0

#     newGrid = [[0 for i in grid[0]] for x in grid]

#     newGrid[len(newGrid) - 1][len(newGrid[0]) - 1] = grid[len(grid) - 1][
#         len(grid[0]) - 1
#     ]

#     for h in range(len(newGrid) - 1, -1, -1):
#         for j in range(len(newGrid[h]) - 1, -1, -1):
#             if (h, j) != (len(newGrid) - 1, len(newGrid[0]) - 1):
#                 n1 = newGrid[h + 1][j] if (h + 1) < len(newGrid) else float("inf")
#                 n2 = newGrid[h][j + 1] if (j + 1) < len(newGrid[0]) else float("inf")
#                 newGrid[h][j] = min(n1, n2) + grid[h][j]

#     return newGrid[0][0]


# g = [[]]

# print(minPathSum(g))

# --------------------------------------------------------------


# Simplified Josephus - edabit


# def josephus(n):

#     survivors = [i for i in range(1, n + 1)]

#     x = 0
#     while True:

#         k = len(survivors)
#         if x >= k:
#             x = 0

#         if k == 1:
#             return survivors[0]

#         survivors.pop(((x % k) + 1) % k)

#         x += 1


# print(josephus(7))

# ----------------------------------------------------------

# Josephus Permutation - edabit


# def who_goes_free(n, k):

#     survivors = [i for i in range(n)]

#     x = 0

#     while True:

#         s = len(survivors)

#         if s == 1:
#             return survivors[0]

#         print(survivors, x)
#         survivors.pop(((x % s) + k - 1) % s)

#         x = ((x % s) + k - 1) % s


# print(who_goes_free(673, 13))


# -----------------------------------------------------------------

# Isomomorphic Strings - edabit


# def is_isomorphic(s, t):

#     hashMap1 = {}
#     hashMap2 = {}

#     if len(s) != len(t):
#         return False

#     for i in range(len(s)):

#         if s[i] in hashMap1:
#             if hashMap1[s[i]] != t[i]:
#                 return False
#         else:
#             hashMap1[s[i]] = t[i]

#         if t[i] in hashMap2:
#             if hashMap2[t[i]] != s[i]:
#                 return False
#         else:
#             hashMap2[t[i]] = s[i]

#     return True

# -------------------------------------------------------------

# Switching Between Pencil - edabit


# def color_pattern_times(cols):

#     count = 0
#     for i in range(len(cols)):

#         if cols[i] == cols[i - 1] or i == 0:
#             count += 2
#         else:
#             count += 3

#     return count


# print(color_pattern_times(["Blue", "Blue", "Blue", "Red", "Red", "Red"]))

# ---------------------------------------------------------------

# Letter Combinations of a Phone Number - leetcode


# def letterCombinations(digits):

#     if len(digits) == 0:
#         return []

#     phone = {
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz",
#     }

#     res = []

#     def backtrack(num, current=""):

#         if len(current) == len(digits):
#             res.append(current)
#             return

#         for i in phone[num[0]]:
#             backtrack(num[1:], current + i)

#     backtrack(digits)

#     return res


# print(letterCombinations("23"))

# ----------------------------------------------------

# Reverse Linked List - leetcode


# def reverseList(head):

#     if head == None:
#         return None

#     node = None
#     next_node = head
#     node_next = head.next if head != None else None

#     while True:

#         next_node.next = node

#         node = next_node

#         next_node = node_next

#         if next_node == None:
#             return node

#         node_next = node_next.next


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# n5 = ListNode(5, None)
# n4 = ListNode(4, n5)
# n3 = ListNode(3, n4)
# n2 = ListNode(2, n3)
# n1 = ListNode(1, n2)

# print(reverseList(n1))

# ---------------------------------------------------------------

# Word Search - leetcode


# def exists(board, word):
#     def backtrack(node, w):

#         if node == None:
#             return False

#         if len(w) == 1 and w == board[node[0]][node[1]]:
#             return True

#         if board[node[0]][node[1]] == w[0]:

#             # This crap makes it alot slower
#             up = (node[0] - 1, node[1]) if node[0] - 1 >= 0 else None
#             down = (node[0] + 1, node[1]) if node[0] + 1 <= len(board) - 1 else None
#             left = (node[0], node[1] - 1) if node[1] - 1 >= 0 else None
#             right = (node[0], node[1] + 1) if node[1] + 1 <= len(board[0]) - 1 else None

#             c = board[node[0]][node[1]]
#             board[node[0]][node[1]] = " "
#             next = [
#                 backtrack(up, w[1:]),
#                 backtrack(down, w[1:]),
#                 backtrack(left, w[1:]),
#                 backtrack(right, w[1:]),
#             ]
#             if any(next):
#                 return True
#             board[node[0]][node[1]] = c
#         else:
#             return False

#     for h in range(len(board)):
#         for j in range(len(board[0])):
#             if backtrack((h, j), word):
#                 return True

#     return False


# bo = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# bo2 = [
#     ["A", "A", "A", "A", "A", "A"],
#     ["A", "A", "A", "A", "A", "A"],
#     ["A", "A", "A", "A", "A", "A"],
#     ["A", "A", "A", "A", "A", "A"],
#     ["A", "A", "A", "A", "A", "A"],
#     ["A", "A", "A", "A", "A", "A"],
# ]
# "AAAAAAAAAAAABAA"
# bo3 = [["a"]]
# bo4 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# bo5 = [["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]]


# better version


# def exist(board, word):
#     ROWS, COLS = len(board), len(board[0])

#     def dfs(i, j, s):
#         if not s:
#             return True
#         if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] != s[0]:
#             return False
#         c = board[i][j]
#         board[i][j] = " "
#         nexts = [
#             dfs(i + 1, j, s[1:]),
#             dfs(i - 1, j, s[1:]),
#             dfs(i, j + 1, s[1:]),
#             dfs(i, j - 1, s[1:]),
#         ]
#         isFound = any(nexts)
#         board[i][j] = c
#         return isFound

#     for i in range(ROWS):
#         for j in range(COLS):
#             if dfs(i, j, word):
#                 return True
#     return False


# print(exists(bo2, "AAAAAAAAAABAA"))

# -------------------------------------------------------------------------

# Find the Secret Word - edabit


# def secretWord(str, n):

#     import itertools

#     alpha = {
#         "a": 1,
#         "b": 2,
#         "c": 3,
#         "d": 4,
#         "e": 5,
#         "f": 6,
#         "g": 7,
#         "h": 8,
#         "i": 9,
#         "j": 10,
#         "k": 11,
#         "l": 12,
#         "m": 13,
#         "n": 14,
#         "o": 15,
#         "p": 16,
#         "q": 17,
#         "r": 18,
#         "s": 19,
#         "t": 20,
#         "u": 21,
#         "v": 22,
#         "w": 23,
#         "x": 24,
#         "y": 25,
#         "z": 26,
#     }

#     triplets = []

#     for i in range(len(str) - 2):
#         count = 0
#         for x in range(3):
#             count += alpha[str[i + x]]
#         triplets.append(count)

#     combinations = [x for x in itertools.combinations(triplets, n)]

#     sequence = []

#     for k in combinations:
#         if len(k) > 1:
#             diff = k[1] - k[0]
#             check = True
#             for j in range(len(k)):
#                 if j > 1 and k[j] - k[j - 1] != diff:
#                     check = False
#                     break
#             if check:
#                 sequence = k
#                 break
#         else:
#             sequence = k
#             break

#     res = ""
#     start = 0

#     for h in sequence:
#         res += str[triplets.index(h, start) + 1]
#         start = triplets.index(h, start)
#     return res


# print(secretWord("fsthorzrevexanstspre", 6), "stress")

# --------------------------------------------------------------------

# Maximum Subarray - leetcode


# def maxSubArray(nums):

#     subArray = nums[0]
#     current = 0

#     for i in nums:

#         if current < 0:
#             current = 0
#         current += i
#         subArray = max(current, subArray)

#     return subArray

# --------------------------------------------

# Reverse Words in a String - leetcode


# def reverseWords(s):

#     new = [x for x in s.split(" ") if x != ""]

#     new.reverse()

#     return " ".join(new)


# print(reverseWords("the sky   is blue"))

# -----------------------------------------

# Spiral Matrix Printing - edabit


# def matrix(num):

#     m = [[0 for x in range(num)] for i in range(num)]

#     row = 0
#     col = 0
#     direction = "right"

#     for i in range(1, (num ** 2) + 1):

#         print(m)

#         if direction == "up" and row >= 0:
#             m[row][col] = i
#             if row == 0 or m[row - 1][col] != 0:
#                 direction = "right"
#                 col += 1
#                 continue
#             row -= 1
#             i += 1

#         if direction == "left" and col >= 0:
#             m[row][col] = i
#             if col == 0 or m[row][col - 1] != 0:
#                 direction = "up"
#                 row -= 1
#                 continue
#             col -= 1
#             i += 1

#         if direction == "down" and row < len(m):
#             m[row][col] = i
#             if row == len(m) - 1 or m[row + 1][col] != 0:
#                 direction = "left"
#                 col -= 1
#                 continue
#             row += 1
#             i += 1

#         if direction == "right" and col < len(m[0]):
#             m[row][col] = i
#             if col == len(m[0]) - 1 or m[row][col + 1] != 0:
#                 direction = "down"
#                 row += 1
#                 continue
#             col += 1
#             i += 1

#     return m


# matrix(10)

# ---------------------------------------------------------------

# Sort Colors - leetcode


# def sortColors(nums):

#     pointer = 0

#     for i in range(len(nums)):
#         if nums[i] == 0:
#             nums.insert(0, nums.pop(i))
#             pointer += 1
#         if nums[i] == 1:
#             nums.insert(pointer, nums.pop(i))

#     return nums


# print(sortColors([1, 2, 0]))

# --------------------------------------------------------


# License Plate - edabit


# def licensePlate(s, n):

#     import math

#     res = []
#     plate = "".join(s.split("-")).upper()

#     for i in range(math.ceil(len(plate) / n)):

#         res.insert(0, plate[-n : len(plate)])

#         plate = plate[0 : len(plate) - n]

#     return "-".join(res)


# print(licensePlate("2-4A0r7-4k", 3))

# ---------------------------------------------------

# Remove Element - leetcode


# def removeElement(nums, val):

#     right = len(nums) - 1
#     left = 0

#     while left <= right:

#         if nums[left] == val:
#             nums[left], nums[right] = nums[right], "_"
#             right -= 1
#             continue
#         left += 1

#     return left


# print(removeElement([1], 1))

# ----------------------------------------------------------

# Hexagonal Grid Distance - edabit


# def hexDistance(grid):

#     lstGrid = [[x for x in row.split(" ") if x != ""] for row in grid]

#     pos = []

#     for count_i, i in enumerate(lstGrid):
#         for count_k, k in enumerate(i):
#             if k == "x":
#                 if count_i < len(lstGrid) / 2:
#                     pos.append((count_i, count_k + len(max(lstGrid, key=len)) - len(i)))
#                 else:
#                     pos.append((count_i, count_k))

#     v = abs(pos[0][0] - pos[1][0])
#     h = abs(pos[0][1] - pos[1][1])
#     d = abs((pos[1][1] - pos[0][1]) + (pos[1][0] - pos[0][0]))

#     return max(h, v, d)


# print(
#     hexDistance(
#         [
#             "    o x o o    ",
#             "   o o o o o   ",
#             "  o o o o o o  ",
#             " o o o o o o o ",
#             "  o o o o o o  ",
#             "   o o o o x   ",
#             "    o o o o    ",
#         ]
#     )
# )

# -----------------------------------------------------------------

# Search Insert Position - leetcode


# def searchInsert(nums, target):

#     start = 0
#     end = len(nums) - 1

#     while start <= end:
#         index = int(round((start + end) / 2))
#         if nums[index] == target:
#             return index

#         if target > nums[index]:
#             start = index + 1
#         else:
#             end = index - 1

#     return start


# print(
#     searchInsert([1, 3, 5, 6], 2)
# )


# -------------------------------------------------------

# Length of Sorting Cycle - edabit

# def cycle_length(lst, n):

#     sorted_lst = sorted(lst)

#     swap = 0

#     num = n

#     while True:

#         current_pos = lst.index(num)
#         true_pos = sorted_lst.index(num)

#         if current_pos == true_pos:
#             return swap

#         lst[current_pos], lst[true_pos] = lst[true_pos], lst[current_pos]

#         num = lst[current_pos]

#         swap += 1


# print(
#     cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 1)
# )

# -------------------------------------------------------------


# Maximum Depth of Binary Tree - leetcode

# def maxDepth(root):

#     if root == None:
#         return 0

#     count = 1
#     s = [root]

#     while True:
#         adj = []
#         for i in s:
#             if i.left != None:
#                 adj.append(i.left)

#             if i.right != None:
#                 adj.append(i.right)

#         if len(adj) == 0:
#             return count

#         s = adj

#         count += 1


# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# n6 = TreeNode(10)
# n5 = TreeNode(7, n6)
# n4 = TreeNode(15)
# n3 = TreeNode(20, n4, n5)
# n2 = TreeNode(9)
# n1 = TreeNode(3, n2, n3)


# print(
#     maxDepth(n1)
# )


# ---------------------------------------------------------

# Missing Number - leetcode

# def missingNumber(nums):

#     hashTable = {}

#     for i in range(len(nums) + 1):
#         hashTable[str(i)] = i

#     print(hashTable)
#     for i in nums:
#         del hashTable[str(i)]

#     return list(hashTable.values())[0]


# print(
#     missingNumber([0, 1, 2, 4])
# )

# Faster Solution with O(1) Space Complexity


# def missingNumber(nums):

#     sum_nums = (len(nums)*(len(nums)+1))/2

#     for i in nums:
#         sum_nums -= i

#     return int(sum_nums
#                )


# print(
#     missingNumber([0, 1, 2, 4])
# )


# --------------------------------------------------------------

# Construct Binary Free from Preorder and Inorder Traversal - leetcode

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):

    print(preorder, inorder)

    if len(inorder) == 0:
        return None

    if(len(inorder) == 1):
        return TreeNode(inorder[0])

    mid = inorder.index(preorder[0])

    return TreeNode(inorder[mid], buildTree(preorder[1:mid], inorder[0:mid]), buildTree(preorder[mid+1:], inorder[mid+1:]))


node = buildTree([1, 2, 3], [3, 2, 1])

res = []


def printTree(root):

    if root == None:
        res.append(None)
        return

    adj = [root.left, root.right]

    res.append(root.val)

    for i in adj:
        printTree(i)


printTree(node)

print(res)
