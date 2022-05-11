// min-cost-to-connect-all-points - leetcode

const minCost = (points) => {
  const distance = (p1, p2) => {
    return Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1])
  }

  let count = 0
  for (let i = 0; i < points.length; i++) {
    let n = []
    for (let j = 0; j < points.length; j++) {
      console.log(j)
      n.push(distance(points[i], points[j]))
    }
    console.log(n)
    count += Math.min(...n)
  }

  return count
}

console.log(
  minCost([
    [3, 12],
    [-2, 5],
    [-4, 1],
  ])
)
