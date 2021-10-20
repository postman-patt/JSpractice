// let promise = new Promise((resolve, reject) => {
//   setTimeout(() => {
//     resolve('success!')
//   }, 1000)
// })

// let p = ''

// promise
//   .then((val) => {
//     p += val
//   })
//   .then(() => console.log(p))

// -----------------------------------------------------------

// var result = ''

// let promise = new Promise((resolve, reject) => {
//   resolve('success!')
// })

// promise.then((val) => {
//   result = val
// })

// console.log(result)

// ---------------------------------------------------------

// const one = () => {
//   console.log('1')
// }

// const two = () => {
//   setTimeout(() => {
//     console.log('2')
//   }, 1000)
// }

// const callbackFunction = async (callback, callback2) => {
//   console.log('3')
//   two()

//   callback()

//   callback2()

//   console.log('5')
// }

// const four = new Promise((resolve, reject) => {
//   setTimeout(() => {
//     resolve('4')
//   }, 1000)
// })

// callbackFunction(four, one)

// one()

// four
//   .then((val) => {
//     console.log(val, 'hello')
//   })
//   .then(() => {
//     console.log('7')
//   })

// const p = new Promise((resolve, reject) => {
//   resolve('4')
// })

// console.log(
//   p.then((val) => {
//     return val
//   })
// )

// console.log('5')

// -------------------------------------------------------------

// const p = async () => {
//   return new Promise((resolve, reject) => {
//     console.log('1234')
//     resolve('10')
//   })
// }

// const longFunction = async () => {
//   return console.log('this ran')
// }

// const asyncFunction = async () => {
//   const x = await p()

//   console.log(x)
//   console.log('3')
// }

// const order = async () => {
//   console.log('14')

//   //   asyncFunction()

//   var promise = new Promise((resolve, reject) => {
//     console.log('promise ran')
//     resolve('9')
//   }).then((val) => {
//     console.log(val)
//   })

//   console.log('5')

//   //.then() returns another promise object
//   console.log(promise)
// }

// order()
// asyncFunction()
// ---------------------------------------

// const p = async () => {
//   return new Promise((resolve, reject) => {
//     resolve('9')
//   })
// }

// const asyncFunction = async () => {
//   const x = await p()

//   return console.log(x)
// }

// const normalFunction = () => {
//   return p().then((val) => {
//     const x = val
//     return console.log(x)
//   })
// }

// // asyncFunction()
// normalFunction()

// //What does .then() do?

// const one = () => {
//   return '1'
// }

// const two = () => {
//   return '2'
// }

// one().then((val) => console.log(`${val} hello`)) //Doesn't work

// ------------------------------------------------------------------------------------------------

//ASYNC/AWAIT <==> PROMISE then() -- Equivalent Functions

//Async/Await

//This function returns a promise
const p = async () => {
  return new Promise((resolve, reject) => {
    console.log('1. Promise ran')
    resolve('2. Promise Resolved Value and console logged by variable')
  })
}

const asyncFunction = async () => {
  const x = await p()

  console.log(x)

  console.log('3. This should be the third console log ran')

  console.log('4. Async/Await function finished')
}

//Promise/then Equivalent

const promiseThen = () => {
  const x = new Promise((resolve, reject) => {
    console.log('1. Promise ran')
    resolve(
      '2. Promise Resolved Value and console logged as resolved value passed through .then()'
    )
  })

  x.then((val) => {
    // Can do x = val (if x was a var we can set the variable to val outside this function scope)
    return val
  }).then((val2) => {
    const x = val2
    //The rest of the function is wrapped in the .then()
    console.log(x)
    console.log('3. This should be the third console log ran')
    console.log('4. Promise/Then function finished')
  })
}

promiseThen()
