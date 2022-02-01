// Promises VIII: Old Callback API - edabit

function saySomething(str) {
  throw 'what the heck'
}

let ERR = ''

const wait = () => new Promise((resolve, reject) => setTimeout(resolve, 1000))
//Note this is essentially a promise within a promise. Set Timeout returns a promise that is resolved first and then this consequently also resolves the outer promise

wait()
  .then(() => saySomething('1 second has passed'))
  .catch((err) => {
    ERR = err
  })

// For function that take in a callback and return a promies such as Set Timeout, if we want to assign the return variable to something you would need to use the above.

// The above functiond demonstrates error handling in the case of callbacks
// wait() function returns a promise that is resolved at the set timeout interval
// When wait function resolves .then () is called, which will call saySomething()
// saySomethig will throw an error, which is then caught by the catch(err)
// error can the be used however you like

const promise1 = (callback) =>
  new Promise((resolve, reject) => resolve(callback())) // acting as the set timeout
const promise2 = () =>
  new Promise(
    (resolve, reject) =>
      promise1(() => {
        return 'hello'
      }).then((val) => {
        resolve(val)
      }) //Resolved first before promise2
  )

promise2().then((v) => console.log('hi', v))

//Everything in promise2 (including the promise1) is resolved first. the value returned from promise1 was then put into another resole() to be passed onto the console.log('hi, v) at the bottom
