# Word Search - leetcode


def exists(board, word):
    def backtrack(node, w):

        if node == None:
            return False

        if len(w) == 1 and w == board[node[0]][node[1]]:
            return True

        if board[node[0]][node[1]] == w[0]:

            # This crap makes it alot slower!!!
            up = (node[0] - 1, node[1]) if node[0] - 1 >= 0 else None
            down = (node[0] + 1, node[1]) if node[0] + 1 <= len(board) - 1 else None
            left = (node[0], node[1] - 1) if node[1] - 1 >= 0 else None
            right = (node[0], node[1] + 1) if node[1] + 1 <= len(board[0]) - 1 else None

            c = board[node[0]][node[1]]
            board[node[0]][node[1]] = " "
            next = [
                backtrack(up, w[1:]),
                backtrack(down, w[1:]),
                backtrack(left, w[1:]),
                backtrack(right, w[1:]),
            ]
            if any(next):
                return True
            board[node[0]][node[1]] = c
        else:
            return False

    for h in range(len(board)):
        for j in range(len(board[0])):
            if backtrack((h, j), word):
                return True

    return False


bo = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
bo2 = [
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
]
"AAAAAAAAAAAABAA"
bo3 = [["a"]]
bo4 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
bo5 = [["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]]


# better version


def exist(board, word):
    ROWS, COLS = len(board), len(board[0])

    def dfs(i, j, s):
        if not s:
            return True
        if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] != s[0]:
            return False
        c = board[i][j]
        board[i][j] = " "
        nexts = [
            dfs(i + 1, j, s[1:]),
            dfs(i - 1, j, s[1:]),
            dfs(i, j + 1, s[1:]),
            dfs(i, j - 1, s[1:]),
        ]
        isFound = any(nexts)
        board[i][j] = c
        return isFound

    for i in range(ROWS):
        for j in range(COLS):
            if dfs(i, j, word):
                return True
    return False


print(exists(bo2, "AAAAAAAAAABAA"))
