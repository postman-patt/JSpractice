const largestIsland = (map) => {
  let visitedNodes = []
  let result = []
  let count = 0

  const adj = ([x, y]) => {
    let adjNodes = []
    for (i = -1; i <= 1; i++) {
      for (j = -1; j <= 1; j++) {
        if (
          x + i < map.length &&
          x + i >= 0 &&
          y + j < map[x].length &&
          y + j >= 0 &&
          map[x + i][y + j] == 1
        ) {
          adjNodes.push([x + i, y + j])
        }
      }
    }

    return adjNodes
  }

  const dfs = (node) => {
    let adjacentNodes = adj(node)
    let visited = visitedNodes.some((a) => {
      return a.every((b, index) => {
        return b == [node[0], node[1]][index]
      })
    })

    if (visited) {
      return
    } else {
      count += 1
      visitedNodes.push(node)
      for (x in adjacentNodes) {
        dfs(adjacentNodes[x])
      }
    }
  }

  for (i in map) {
    for (j in map[i]) {
      var currentNode = [Number(i), Number(j)]
      //Check if [i, j] is in visitedNodes
      var isVisited = visitedNodes.some((a) => {
        return a.every((b, index) => {
          return b == [i, j][index]
        })
      })

      //Find unvisited nodes
      if (map[i][j] == 1 && !isVisited) {
        //Run DFS
        dfs(currentNode)
        result.push(count)
        count = 0
      }
    }
  }

  console.log(result)
}

const map1 = [
  [0, 1, 0],
  [0, 1, 1],
  [0, 1, 1],
]

const map2 = [
  [1, 0, 0],
  [0, 0, 0],
  [0, 0, 1],
]

const map3 = [
  [1, 0, 0],
  [1, 0, 0],
  [1, 0, 1],
]

const map4 = [
  [1, 0, 0, 0],
  [1, 0, 0, 1],
  [1, 0, 1, 1],
  [1, 0, 0, 1],
  [1, 0, 1, 1],
]
largestIsland(map1)
largestIsland(map2)
largestIsland(map3)
largestIsland(map4)
