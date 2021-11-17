// Sliding window version

const maxArea = (height) => {
  var right = height.length - 1
  var left = 0
  let res = 0

  while (left < right) {
    const area = (right - left) * Math.min(height[right], height[left])
    if (height[left] < height[right]) {
      left += 1
    } else {
      right -= 1
    }

    if (area > res) {
      res = area
    }
  }

  return res
}

console.log(maxArea([2, 3, 4, 5, 18, 17, 6]))
