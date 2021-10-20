// https://leetcode.com/problems/restore-ip-addresses/discuss/1510890/Python-Backtracking-Solution-faster-than-90

const restoreIPaddress = (s) => {
  //Backtracking
  let res = []

  let N = s.length

  const backtrack = (temp, pos, dot) => {
    console.log(temp, pos, dot)

    if (pos > N) {
      return
    }

    if (pos == N && dot == 4) {
      res.push(temp)
      return
    }

    if ((pos == N && dot < 4) || (pos < N && dot == 4)) {
      return
    }

    if (s[pos] == '0') {
      backtrack(temp.concat([s.slice(pos, pos + 1)]), pos + 1, dot + 1)
      return
    }

    //trying 1, 2 and 3 numbers
    backtrack(temp.concat([s.slice(pos, pos + 1)]), pos + 1, dot + 1)
    backtrack(temp.concat([s.slice(pos, pos + 2)]), pos + 2, dot + 1)

    if (Number(s.slice(pos, pos + 3)) <= 255) {
      backtrack(temp.concat([s.slice(pos, pos + 3)]), pos + 3, dot + 1)
    }
  }

  backtrack([], 0, 0)

  return res
}

console.log(restoreIPaddress('25525511135'))
