
// min-cost-to-connect-all-points - leetcode

// const minCost = (points) => {
//   const distance = (p1, p2) => {
//     return Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1])
//   }

//   let count = 0
//   for (let i = 0; i < points.length; i++) {
//     let n = []
//     for (let j = 0; j < points.length; j++) {
//       console.log(j)
//       n.push(distance(points[i], points[j]))
//     }
//     console.log(n)
//     count += Math.min(...n)
//   }

//   return count
// }

// console.log(
//   minCost([
//     [3, 12],
//     [-2, 5],
//     [-4, 1],
//   ])
// )

// ---------------------------------------------------------------------

// Running Sum - Leetcode

// const runningSum = (nums) => {
//   if (nums.length == 0) {
//     return []
//   }

//   let res = [nums[0]]

//   for (let i = 1; i < nums.length; i++) {
//     res.push(nums[i] + res[res.length - 1])
//   }

//   return res
// }

// console.log(runningSum([1, 2, 3, 4]))

// -------------------------------------------------------------------

// 1695. Maximum Erasure Value - leetcode

// const maximumUniqueSubarray = (nums) => {
//   let set = new Set()
//   let subArr = []
//   let curr_sum = 0
//   let max = 0

//   for (let i = 0; i < nums.length; i++) {
//     if (set.has(nums[i])) {
//       if (curr_sum > max) {
//         max = curr_sum
//       }

//       while (set.has(nums[i]) && subArr.length > 0) {
//         let s = subArr.shift()
//         curr_sum -= s
//         set.delete(s)
//       }

//       set.add(nums[i])
//       subArr.push(nums[i])
//       curr_sum += nums[i]
//     } else {
//       set.add(nums[i])
//       subArr.push(nums[i])
//       curr_sum += nums[i]
//     }

//   }

//   return Math.max(max, curr_sum)
// }

// console.log(maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))
// 4, 2, 3, 4, 5, 6, 4, 7, 3, 2, 5, 9, 8, 3, 4,
// 4, 6, 9, 9, 14, 20, 15, 22, 25, 27, 18, 27, 30,

// 4, 6, 6, 11, 17

// --------------------------------------------------------------------

// const t = [
//   [1, 2, 3, 4, 5],
//   [6, 7, 8, 9, 10],
//   [11, 12, 13, 14, 15],
// ]

// const test = (search) => {
//   dance: for (let i = 0; i < t.length; i++) {
//     for (let j = 0; j < search.length; j++) {
//       if (search[j] != null) {
//         if (search[j] != t[i][j]) {
//           continue dance
//         }
//       }
//     }
//     return i
//   }
//   return null
// }

// console.log(test([11]))


// ------------------------------------------------------------------


// 509. Fibonacci Number - leetcode

// const fib = (n) => {
//   if( n <= 1){
//     return n
//   } else {
//     return fib(n -1) + fib(n-2)
//   }
// }

// console.log(fib(3))

// ------------------------------------------------------------------


// 746. Min Cost Climbing Stairs - leetcode

const minCostToClimbStairs = (stairs) => {

    stairs.push(0)

    let minCost = [stairs[0], stairs[1]]

    for(let i = 2; i < stairs.length; i ++){
        let prev1 = minCost[i-2]
        let prev2 = minCost[i-1]

        if (prev1 < prev2){
            minCost.push(stairs[i] + prev1)
        } else {
            minCost.push(stairs[i]+ prev2)
        }
        
    }

    

    return minCost[minCost.length -1]

}


console.log(
minCostToClimbStairs([10,15,20]))

// 581. Shortest Unsorted Continuous Subarray

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
