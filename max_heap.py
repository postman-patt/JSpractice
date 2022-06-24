
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
