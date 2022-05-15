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
