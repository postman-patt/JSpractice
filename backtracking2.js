// Permutations - leetcode

// Backtracking

const permute = (nums) => {
  let res = []
  const backtracking = (n, r = []) => {
    if (n.length == 0) {
      res.push(r)
    }
    for (let i = 0; i < n.length; i++) {
      backtracking(n.slice(0, i).concat(n.slice(i + 1)), [...r, n[i]])
    }
  }

  backtracking(nums)

  return res
}

console.log(permute([1, 2, 3]))

// Always Always use "let" "var" and "const". If these are NOT used, the variable is globally scoped, which means you can access from any functions, anywhere. See below example for demo

// const j = () => {
//   const m = () => {
//     x = 10
//   }
//   m()
// }

// j()

// console.log(x)
// ouput: 10
