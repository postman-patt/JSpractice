
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
=======
// 581. Shortest Unsorted Continuous Subarray

const findUnsortedSubarray = (nums) => {
  const sortedNums = [...nums].sort((a, b) => {
    return a - b
  })
  console.log(sortedNums, nums)
  let left = 0
  let right = nums.length - 1

  while (left < right) {
    if (nums[left] == sortedNums[left]) {
      left++
    }

    if (nums[right] == sortedNums[right]) {
      right--
    }

    if (nums[left] != sortedNums[left] && nums[right] != sortedNums[right]) {
      return right - left + 1
    }
  }

  return 0
}

console.log(findUnsortedSubarray([1, 2, 4, 5, 3]))

