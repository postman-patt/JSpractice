class Battleship {
  constructor(scheme, input) {
    this.scheme = scheme
    this.input = input
    this.hit = 0
    this.score = 0
    this.sunkCruisers = 0
    this.bo = this.buildboard()
  }

  buildboard() {
    var bo = [
      ['○', '○', '○', '○', '○'],
      ['○', '○', '○', '○', '○'],
      ['○', '○', '○', '○', '○'],
      ['○', '○', '○', '○', '○'],
      ['○', '○', '○', '○', '○'],
    ]

    for (var i in this.scheme) {
      var y = this.scheme[i].charCodeAt(0) - 65
      var x = Number(this.scheme[i][1]) - 1
      bo[y][x] = '●'
    }

    for (var h in this.input) {
      var y = this.input[h].charCodeAt(0) - 65
      var x = Number(this.input[h][1]) - 1
      if (bo[y][x] == '●') {
        bo[y][x] = '☀'
        this.hit += 1
        this.score += 1
      } else {
        bo[y][x] = '☼'
      }
    }

    for (var m in this.input) {
      var y = this.input[m].charCodeAt(0) - 65
      var x = Number(this.input[m][1]) - 1
      if (bo[y][x] == '☀' && this.adj([x, y], bo)) {
        this.sunkCruisers += 1 / 2
        this.score += 1
      }
    }

    return bo
  }

  adj(pos, bo) {
    let x = pos[0]
    let y = pos[1]
    var left = x - 1 >= 0 ? bo[y][x - 1] : 0
    var right = x + 1 < bo[y].length ? bo[y][x + 1] : 0
    var bottom = y + 1 < bo.length ? bo[y + 1][x] : 0
    var top = y - 1 >= 0 ? bo[y - 1][x] : 0

    if (left == '☀' || right == '☀' || top == '☀' || bottom == '☀') {
      return true
    } else {
      return false
    }
  }

  board() {
    return this.bo
  }

  hits() {
    return this.hit
  }

  points() {
    return this.score
  }

  sunk() {
    return this.sunkCruisers
  }
}

const s1 = ['A1', 'C1', 'B2', 'B3', 'D2', 'E2', 'E4', 'E5', 'A5']
const input1 = ['A1', 'B2', 'C3', 'D4', 'E5', 'E4']
const s2 = ['A1', 'C1', 'B2', 'B3', 'D2', 'E2', 'E4', 'E5', 'A5']
const input2 = ['A1', 'B2', 'C3', 'D4', 'E5', 'E4']
const s3 = ['A2', 'A4', 'C1', 'C2', 'E3', 'C4', 'C5', 'D3', 'E5']
const input3 = ['A1', 'B1', 'D1', 'E1', 'A3', 'A4']
const s4 = ['A1', 'B1', 'D1', 'E1', 'A3', 'A4', 'D3', 'E4', 'D5']
const input4 = ['A2', 'B4', 'C1', 'D3', 'E5', 'A5']
const b2 = new Battleship(s4, input3)
const b3 = new Battleship(s1, input1)

console.log(b2)
console.log(b3)

// console.log(b1.board())
