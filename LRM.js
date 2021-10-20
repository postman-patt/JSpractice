//Heuristic Algorithms for Balanced Multi-way Number Partitioning

//BNMP Balanced Multi-way Partitiioning Approach

//Given array p with relatively low spread
const p1 = [
  20, 14, 13, 16, 13, 2, 6, 7, 12, 14, 15, 16, 16, 3, 2, 15, 16, 7, 3, 32, 26,
]

//Array with high spread/variability
const p2 = [40, 30, 13, 16, 13, 2, 6, 7, 12, 50]

// BNMP
const bnmp = (p, groups) => {
  let result = []

  const sortP = p.sort((a, b) => {
    return b - a
  })

  for (j = 0; j < groups; j++) {
    result.push([])
  }

  let count = 0
  let directionUp = true
  for (i in p) {
    if (directionUp) {
      result[count].push(sortP[i])
      count += 1
      if (count >= groups) {
        directionUp = false
      }
    } else {
      count -= 1
      result[count].push(sortP[i])

      if (count <= 0) {
        directionUp = true
      }
    }
  }

  return result.map((item) => {
    return item.reduce((a, b) => {
      return a + b
    })
  })
}

console.log(
  'Balanced Multi-way Partitiioning Approach - Low Spread - ',
  bnmp(p1, 4)
)
console.log(
  'Balanced Multi-way Partitiioning Approach - Low Spread - ',
  bnmp(p2, 4)
)

//PMWS - Pats multi-way sorting

const pmws = (p, groups) => {
  let result = []

  const sortP = p.sort((a, b) => {
    return b - a
  })

  for (j = 0; j < groups; j++) {
    result.push([])
  }

  for (i in p) {
    var currentState = result.map((item) => {
      if (item.length !== 0) {
        return item.reduce((a, b) => {
          return a + b
        })
      } else {
        return 0
      }
    })

    var indexOfLowest = currentState.indexOf(
      [...currentState].sort((a, b) => {
        return a - b
      })[0]
    )
    result[indexOfLowest].push(sortP[i])
  }

  return result.map((item) => {
    return item.reduce((a, b) => {
      return a + b
    })
  })
}

console.log("Pat's Multi-way Partitioning - Low Spread -", pmws(p1, 4))
console.log("Pat's Multi-way Partitioning - High Spread -", pmws(p2, 4))
