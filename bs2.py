# Binary Search

# Search a 2D Matrix - leetcode


def searchMatrix(matrix, target):

    start, end = 0, len(matrix) - 1

    while start <= end:
        mid = round((start + end) / 2)

        print(type(mid))

        if target in matrix[mid]:
            return True

        if target > max(matrix[mid]):
            start = mid + 1
        else:
            end = mid - 1

    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 34))
