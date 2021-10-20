def knightBFS(x1, y1, x2, y2):
    start = (x1, y1)
    end = (x2, y2)
    queue = [[start]]

    def adj(node):
        adjacentNodes = []
        moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for x in moves:
            if (
                node[0] + x[0] >= 1
                and node[0] + x[0] <= 8
                and node[1] + x[1] >= 1
                and node[1] + x[1] <= 8
            ):
                transNode = tuple(map(lambda i, j: i + j, x, node))
                if (
                    transNode not in [a for item in queue for a in item]
                    and transNode not in adjacentNodes
                ):
                    adjacentNodes.append(transNode)
        return adjacentNodes

    for i, value1 in enumerate(queue):
        sublist = []
        for value2 in value1:
            if value2 == end:
                return i
            else:
                sublist += adj(value2)
        queue.append(sublist)


print(knightBFS(8, 8, 3, 3))

# What is a better way of keeping track of which layer you are on in BFS?
