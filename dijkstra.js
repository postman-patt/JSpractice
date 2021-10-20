const sampleRoads = {
  graph: {
    directed: false,
    nodes: [
      { id: 0 },
      { id: 1 },
      { id: 2 },
      { id: 3 },
      { id: 4 },
      { id: 5 },
      { id: 6 },
      { id: 7 },
      { id: 8 },
      { id: 9 },
    ],
    edges: [
      {
        source: 1,
        target: 6,
        label: 'Oak Street',
        metadata: {
          distance: 5,
        },
      },
      {
        source: 6,
        target: 8,
        label: 'Oak Street',
        metadata: {
          distance: 6,
        },
      },
      {
        source: 8,
        target: 9,
        label: 'Oak Street',
        metadata: {
          distance: 11,
        },
      },
      {
        source: 8,
        target: 7,
        label: 'Robin Way',
        metadata: {
          distance: 3,
        },
      },
      {
        source: 7,
        target: 4,
        label: 'Robin Way',
        metadata: {
          distance: 5,
        },
      },
      {
        source: 6,
        target: 7,
        label: 'Mountain Road',
        metadata: {
          distance: 8,
        },
      },
      {
        source: 7,
        target: 9,
        label: 'Mountain Road',
        metadata: {
          distance: 9,
        },
      },
      {
        source: 4,
        target: 3,
        label: 'National Street',
        metadata: {
          distance: 6,
        },
      },
      {
        source: 1,
        target: 0,
        label: 'Sunrise Drive',
        metadata: {
          distance: 4,
        },
      },
      {
        source: 0,
        target: 3,
        label: 'Short Street',
        metadata: {
          distance: 3,
        },
      },
      {
        source: 5,
        target: 4,
        label: 'Rickety Creek',
        metadata: {
          distance: 7,
        },
      },
      {
        source: 4,
        target: 0,
        label: 'Rickety Creek',
        metadata: {
          distance: 5,
        },
      },
      {
        source: 9,
        target: 5,
        label: 'Uphill Grove',
        metadata: {
          distance: 6,
        },
      },
      {
        source: 5,
        target: 2,
        label: 'Uphill Grove',
        metadata: {
          distance: 5,
        },
      },
      {
        source: 2,
        target: 3,
        label: 'Uphill Grove',
        metadata: {
          distance: 7,
        },
      },
    ],
  },
}

const navigator = (road, start, end) => {
  const { edges } = road.graph
  const { nodes } = road.graph
  var table = {}
  var visited = []
  var unvisited = []

  // Populate unvisited nodes
  for (x in nodes) {
    unvisited.push(nodes[x].id)
  }

  // Populate Table
  for (i in nodes) {
    table[nodes[i].id] = { shortestDistance: Infinity, path: null }
  }

  // Instantiate starting node distance as 0
  table[start].shortestDistance = 0

  // Visit neighbouring nodes
  while (unvisited.length > 0) {
    // Get node with shortest distance
    var currentNode = Object.keys(table)
      .filter((x) => {
        for (a in unvisited) {
          if (x == unvisited[a]) {
            return true
          }
        }
      })
      .sort((a, b) => {
        return table[a].shortestDistance - table[b].shortestDistance
      })[0]

    for (q in edges) {
      var dist =
        table[currentNode].shortestDistance + edges[q].metadata.distance

      //If source/target match current node and corresponding source/target distance + current node shortest distance is less than target/source shortest distance in the table then add to table
      if (
        edges[q].source == currentNode &&
        dist < table[edges[q].target].shortestDistance
      ) {
        table[edges[q].target].shortestDistance = dist
        table[edges[q].target].path = currentNode
      } else if (
        edges[q].target == currentNode &&
        dist < table[edges[q].source].shortestDistance
      ) {
        table[edges[q].source].shortestDistance = dist
        table[edges[q].source].path = currentNode
      }
    }

    visited.push(currentNode)

    unvisited.splice(
      unvisited.findIndex((id) => {
        return id == currentNode
      }),
      1
    )
  }

  //We use the visited array to determine the path taken.
  //Shortets path taken = everything before the its position within the visited array
  //For the starting point, this would be null

  var path = [end]
  for (i in Object.keys(table)) {
    if (path[0] == start) {
      break
    } else {
      path.unshift(table[path[0]].path)
    }
  }

  return {
    distance: Number(table[end].shortestDistance),
    path: path.map((z) => {
      return Number(z)
    }),
  }
}

console.log(navigator(sampleRoads, 6, 2))
