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
# Implements Counting Sort
# Counting sort is essentially a frequency map
# Initialize array of all possible values, then loops through array and increment for each value
# Example, for list [1, 1, 2, 2, 4, 5, 6]
# Counting sort list [2, 2, 0, 1, 1, 1] - each index in this list correlates to a value in original list
# Median = index where sum(frequency[:index]) >= sum(frequency)/2
# To find median in a counting sort, loop through frequencies and find index where sum of previous is greater than sum(frequencies)/2


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
