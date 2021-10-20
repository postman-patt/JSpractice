//These two work as it references the exports object and assigns a value to the property within the export object ( a and b )

// module.exports.a = firstName = (name) => {
//   console.log('firstName function')
//   console.log(name)
// }

// exports.b = lastName = (name) => {
//   console.log('lastName function')
//   console.log(name)
// }

//This works as it assigns the entire object of the module.exports property to the function. You wont be able to set other properties as it assigns the whole property to the funtion.
// module.exports = firstName = (name) => {
//   console.log('firstName function')
//   console.log(name)
// }

//This does not work as the equals sign (=) will reassign the exports constant to function. It no longer represents anyting within the modules.exports object anymore
exports = lastName = (name) => {
  console.log('lastName function')
  console.log(name)
}

//The most important aspects is to understand that by default, "exports" is a shortcut that reference module.exports. If you reassign it to another variable the shortcut will no lonegr work.
