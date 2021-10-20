const products = [
  { number: 1, price: 100, name: 'Orange juice' },
  { number: 2, price: 200, name: 'Soda' },
  { number: 3, price: 150, name: 'Chocolate snack' },
  { number: 4, price: 250, name: 'Cookies' },
  { number: 5, price: 180, name: 'Gummy bears' },
  { number: 6, price: 500, name: 'Condoms' },
  { number: 7, price: 120, name: 'Crackers' },
  { number: 8, price: 220, name: 'Potato chips' },
  { number: 9, price: 80, name: 'Small snack' },
]

const vendingMachine = (products, money, code) => {
  //Binary Search
  let start = 0,
    end = products.length - 1

  let res

  while (start <= end) {
    let mid = Math.floor((start + end) / 2)
    if (code == products[mid].number) {
      res = mid
      break
    } else if (code > products[mid].number) {
      start = mid + 1
    } else {
      end = mid - 1
    }
  }

  console.log(res)
  const coins = [500, 200, 100, 50, 20, 10]
  if (res >= 0) {
    if (products[res].price > money) {
      return 'Not enough money for this product'
    } else {
      let change = []
      let changeSum = money - products[res].price
      while (changeSum > 0) {
        for (i in coins) {
          if (coins[i] <= changeSum) {
            changeSum -= coins[i]
            change.push(coins[i])
            break
          }
        }
      }
      return {
        product: products[res].name,
        change: change.sort((a, b) => {
          return b - a
        }),
      }
    }
  } else {
    return 'Enter a valid product number'
  }
}

console.log(vendingMachine(products, 100, 1))
