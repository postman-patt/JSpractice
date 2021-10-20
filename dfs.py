
maze1 = [
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0],
]


def canExit(maze):
    start = (0, 0)
    visitedNodes = []

    def adj(node):
        adjLst = []
        transformations = [
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 0),
        ]

        for i in transformations:
            trans = tuple(map(lambda y, x: x + y, node, i))
            if (
                trans[1] >= 0
                and trans[1] < len(maze)
                and trans[0] >= 0
                and trans[0] < len(maze[0])
                and maze[trans[1]][trans[0]] == 0
                and trans not in visitedNodes
            ):
                adjLst.append(trans)

        return adjLst

    def dfs(currentNode):
        adjList = adj(currentNode)

        if currentNode == (len(maze[0]) - 1, len(maze) - 1):
            return True

        if len(adjList) == 0:
            return
        else:
            for x in adjList:
                visitedNodes.append(currentNode)
                # If you do 'return dfs(x)' it will recursively return none when it hits a len(adjList == 0), we need it to continue the loop in order to continue searching the path.
                if dfs(x):
                    return True

        return False

    return dfs(start)


print(canExit(maze1))