
# 329. Longest increasing path in a matrix - leetcode - HARD

# Combinations of BFS, DP and Memoisation

def longestIncreasingPath(matrix):

    transformations = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Dict of shortest paths for each nodes of the matrix
    paths = {}

    def bfs(node):

        x, y = node[0], node[1]

        # If (x, y) in paths then return the shortest path from dict
        if (x, y) in paths:
            return paths[(x, y)]

        # Find all nodes to traverse for a given node
        nodes_to_traverse = []

        for i in transformations:
            row, col = (x + i[0], y + i[1])

            if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]) and matrix[row][col] > matrix[x][y]:
                nodes_to_traverse.append((row, col))

        # If there are no nodes to travel to then we can assume it is the end of a path. Return the current node
        if len(nodes_to_traverse) == 0:
            paths[(x, y)] = [matrix[x][y]]
            return [matrix[x][y]]

        # Traverse each valid node
        for j in nodes_to_traverse:

            # Add current node with the path found in the BFS
            p = [matrix[x][y]] + bfs(j)

            #Check if the path found, p, is longer then the one currently available in paths dict. If not in paths dict then add.
            if (x, y) in paths:
                if len(paths[(x, y)]) < len(p):
                    paths[(x, y)] = p
            else:
                paths[(x, y)] = p

        # Return the current longest path to the node that called the BFS
        return paths[(x, y)]

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            bfs((r, c))

    return len(max([k for k in paths.values()], key=len))


print(
longestIncreasingPath([[1]])
)