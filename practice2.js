// 581. Shortest Unsorted Continuous Subarray - leetcode

// const findUnsortedSubarray = (nums) => {
//   const sortedNums = [...nums].sort((a, b) => {
//     return a - b
//   })
//   console.log(sortedNums, nums)
//   let left = 0
//   let right = nums.length - 1

//   while (left < right) {
//     if (nums[left] == sortedNums[left]) {
//       left++
//     }

//     if (nums[right] == sortedNums[right]) {
//       right--
//     }

//     if (nums[left] != sortedNums[left] && nums[right] != sortedNums[right]) {
//       return right - left + 1
//     }
//   }

//   return 0
// }

// console.log(findUnsortedSubarray([1, 2, 4, 5, 3]))

// ----------------------------------------------------

// JS10-bitwise - HackerRank

// const getMaxLessThanK = (n, k) => {
//   let res = 0

//   for (let a = 1; a < n; a++) {
//     for (let b = a + 1; b <= n; b++) {
//       let sub = a & b
//       if (sub < k && sub > res) {
//         res = a & b
//       }
//     }
//   }

//   return res
// }

// -------------------------------------------------------

// 162. Find Peak Element - leetcode

// const findPeakElement = (nums) => {
//   for (let i = 1; i < nums.length - 1; i++) {
//     if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1]) {
//       return i
//     }
//   }

//   if (nums.length > 1 && nums[nums.length - 1] > nums[nums.length - 2]) {
//     return nums.length - 1
//   }
//   return 0
// }

// ----------------------------------------------------

// 2D Array - HackerRank

const hourglassSum = (arr) => {
  transformations = [
    [-1, 1],
    [0, 1],
    [1, 1],
    [-1, -1],
    [0, -1],
    [1, -1],
    [0, 0],
  ]

  const hSum = (node) => {
    let count = 0

    for (let i = 0; i < transformations.length; i++) {
      let row = node[0] + transformations[i][1]
      let col = node[1] + transformations[i][0]

      count += arr[row][col]
    }

    return count
  }

  let res = []

  for (let r = 1; r < arr.length - 1; r++) {
    for (let c = 1; c < arr[0].length - 1; c++) {
      res.push(hSum([r, c]))
    }
  }

  return Math.max(...res)
}

console.log(
  hourglassSum([
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
  ])
)
