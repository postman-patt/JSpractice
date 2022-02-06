// sampleArray = ['codikng', 'crackers', 'edawbit', 'celekbration']

// const longestWord = (sampleArray) => {
//   const invalidLetters = ['k', 'm', 'v', 'w', 'x']

//   const validWords = sampleArray.filter((item) => {
//     const word = item.split('')
//     const isInvalid = word.some((letter) => {
//       isTrue = invalidLetters.some((invalidLetter) => letter === invalidLetter)

//       if (isTrue) {
//         return true
//       }
//     })

//     if (isInvalid !== true) {
//       return item
//     }
//   })

//   const longest = validWords.sort((a, b) => {
//     return b.length - a.length
//   })[0]

//   if (longest) {
//     console.log(longest)
//   } else {
//     console.log('')
//   }
// }
// longestWord(sampleArray)

// -------------------------------------------------------------------------

// Above code rewritten - 15-01-22

// Longest Word in a 7 Segment Display - edabit

// const longest7SegmentWord = (arr) => {
//   return (
//     arr
//       .filter((item) => {
//         return !/[kmvwx]/g.test(item)
//       })
//       .sort((a, b) => {
//         return b.length - a.length
//       })[0] || ''
//   )
// }
// console.log(longest7SegmentWord(['velocity', 'mackerel', 'woven', 'kingsmen']))
//---------------------------------------------------------------------------

// const sumDigProd = (num1, num2) => {
//   sumTotal = num1 + num2
//   sumNum1 = +sumTotal.toString().split('')[0]
//   sumNum2 = +sumTotal.toString().split('')[1]

//   const prodNums = (num1, num2) => {
//     total = num1 * num2
//     prodNum1 = +total.toString().split('')[0]
//     prodNum2 = +total.toString().split('')[1]

//     if (prodNum1 && prodNum2) {
//       prodNums(prodNum1, prodNum2)
//     } else {
//       console.log(prodNum1)
//     }
//   }

//   prodNums(sumNum1, sumNum2)
// }
// sumDigProd(16, 28)

// const sumDigProd = (...args) => {
//   const sumTotal = args.reduce((total, num) => {
//     return total + num
//   })

//   const arrayTotal = sumTotal
//     .toString()
//     .split('')
//     .map((x) => +x)

//   const prodNums = (array) => {
//     if (array.length === 1) {
//       console.log(array[0])
//     } else {
//       prodTotal = array.reduce((total, num) => {
//         return total * num
//       })

//       const arrayProdTotal = prodTotal
//         .toString()
//         .split('')
//         .map((x) => +x)
//       prodNums(arrayProdTotal)
//     }
//   }

//   prodNums(arrayTotal)
// }
// sumDigProd(8, 16, 89, 3)

//------------------------------------------------------------------

// const primalStrength = (n) => {
//   const isPrime = (n) => {
//     for (i = 2; i < n; i++) {
//       if (n % i === 0) {
//         return false
//       }
//       return true
//     }
//   }

//   const primeBefore = (num) => {
//     for (i = num; num < i >= 0; i--) {
//       let prime = true
//       for (j = 2; j < i; j++) {
//         if (i % j == 0 && i !== j) {
//           prime = false
//           break
//         }
//       }
//       if (prime == true && i !== num) {
//         return i
//       }
//     }
//   }

//   const primeAfter = (num) => {
//     for (i = num; i; i++) {
//       let prime = true
//       for (j = 2; j < i; j++) {
//         if (i % j == 0 && i !== j) {
//           prime = false
//           break
//         }
//       }
//       if (prime == true && i !== num) {
//         return i
//       }
//     }
//   }

//   if (isPrime(n)) {
//     const primeBeforeNum = primeBefore(n)
//     const primeAfterNum = primeAfter(n)

//     switch (true) {
//       case n - primeBeforeNum > primeAfterNum - n:
//         console.log('Strong')
//         break
//       case n - primeBeforeNum < primeAfterNum - n:
//         console.log('Weak')
//         break
//       case n - primeBeforeNum == primeAfterNum - n:
//         console.log('Balanced')
//         break
//     }
//   } else {
//     console.log('Not a prime....')
//   }
// }

// primalStrength(22)

//---------------------------------------------------------------

// const doubleSwap = (string, c1, c2) => {
//   const arrayString = string.split('')
//   const newArrayString = arrayString.map((char) => {
//     switch (true) {
//       case char == c1:
//         return c2
//       case char == c2:
//         return c1
//       default:
//         return char
//     }
//   })

//   const newString = newArrayString.reduce((string, char) => {
//     return (string += char)
//   })

//   console.log(newString)
// }

// doubleSwap('random w#rds writt&n h&r&', '#', '&')

//---------------------------------------------------------------

// const isAstonishing = (num) => {
//   if (num < 9) {
//     console.log('Number cannot be partitioned')
//   } else {
//     const partition = (num) => {
//       let partitions = []
//       const number = num.toString()
//       for (i = 1; i < number.length; i++) {
//         const p1 = +number.slice(0, i)
//         const p2 = +number.slice(i)
//         partitions.push({ p1, p2 })
//       }
//       return partitions
//     }

//     const count = (num1, num2) => {
//       let num = 0
//       for (i = num1; i <= num2; i++) {
//         num += i
//       }
//       return num
//     }

//     const partitions = partition(num)

//     let valid = false
//     let pos = false
//     partitions.forEach((part) => {
//       switch (true) {
//         case part.p1 > part.p2:
//           if (count(part.p2, part.p1) == num) {
//             valid = true
//             pos = 'BA-Astonishing'
//           }
//         case part.p2 > part.p1:
//           if (count(part.p1, part.p2) == num) {
//             valid = true
//             pos = 'AB-Astonishing'
//           }
//         default:
//       }
//     })

//     console.log(pos)
//   }
// }

// isAstonishing(2665444422)

//-------------------------------------------------------------------

// const sampleArray = [1, 1, 1, 1, -3, -4]

// const isPositiveDominant = (array) => {
//   const uniqueOnly = Array.from(new Set(array))

//   let posCount = 0
//   let negCount = 0

//   for (i = 0; i < uniqueOnly.length; i++) {
//     if (uniqueOnly[i] > 0 && uniqueOnly[i] !== 0) {
//       posCount += 1
//     } else if (uniqueOnly[i] < 0 && uniqueOnly[i] !== 0) {
//       negCount += 1
//     }
//   }

//   switch (true) {
//     case posCount > negCount:
//       console.log('Positive Dominant')
//       break
//     case negCount > posCount:
//       console.log('Negative Dominant')
//       break
//     default:
//       console.log('Balanced')
//       break
//   }
// }

// isPositiveDominant(sampleArray)

//--------------------------------------------------------------

// const trackRobot = (...args) => {
//   const directions = [...args]
//   const dirNorthSouth = []
//   const dirEastWest = []

//   for (i = 0; i < directions.length; i++) {
//     if (i % 2 == 0 || i == 0) {
//       dirNorthSouth.push(directions[i])
//       dirEastWest.push(directions[i + 1])
//     }
//   }

//   const trueNorthSouth = dirNorthSouth
//     .filter((element) => {
//       return element !== undefined
//     })
//     .map((dir, index) => {
//       if ((index + 1) % 2 == 0 && index !== 0) {
//         return -dir
//       } else {
//         return dir
//       }
//     })
//     .reduce((total, item) => {
//       return (total += item)
//     })

//   const trueEastWest = dirEastWest
//     .filter((element) => {
//       return element !== undefined
//     })
//     .map((dir, index) => {
//       if ((index + 1) % 2 == 0 && index !== 0) {
//         return -dir
//       } else {
//         return dir
//       }
//     })
//     .reduce((total, item) => {
//       return (total += item)
//     })

//   console.log([trueEastWest, trueNorthSouth])
// }

// trackRobot(-10, 20, 10)
// trackRobot(20, 30, 10, 40)
// trackRobot(0, 0)

//---------------------------------------------------------

// const balance = (str) => {
//   const alphabet = 'abcdefghijklmnopqrstuvwxyz'

//   const firstSplit = str.slice(0, Math.floor(str.length / 2)).split('')
//   const secondSplit = str
//     .slice(-Math.floor(str.length / 2), str.length)
//     .split('')

//   const num1 = firstSplit
//     .map((letter) => {
//       const index = alphabet.indexOf(letter) + 1
//       return index
//     })
//     .reduce((total, value) => (total += value))

//   const num2 = secondSplit
//     .map((letter) => {
//       const index = alphabet.indexOf(letter) + 1
//       return index
//     })
//     .reduce((total, value) => (total += value))

//   if (num1 === num2) {
//     return console.log(true)
//   } else {
//     return console.log(false)
//   }
// }
// balanced('zips')
// balanced('brake')
// balance('gfrffewfg')

//----------------------------------------------------------------

// const overlap = (s1, s2) => {
//   const s1ToLower = s1.toLowerCase()
//   const s2ToLower = s2.toLowerCase()

//   switch (true) {
//     case s2.length >= s1.length:
//       const isIndex = s2ToLower.indexOf(s1ToLower)
//       if (s2.length - isIndex == s1.length) {
//         return console.log(true)
//       }
//     case s2.length <= s1.length:
//       const index = s1ToLower.indexOf(s2ToLower)
//       if (s1.length - index == s2.length) {
//         return console.log(true)
//       }
//     default:
//       return console.log(false)
//   }
// }

// overlap('ABC', "Ican'tsingmyABC")
//--------------------------------------------------------------------

//"function name() {}" ➞ "const name = () => {dfefe}"

// const convertFn = (str) => {
//   let arrow = /=>/
//   const checkArrow = arrow.test(str)

//   if (checkArrow) {
//     let arrowFn = str.split(' ')
//     let params = str.match(/\((.*?)\)/)[0]
//     let fn = str.slice(str.indexOf('{'))
//     let regFn = `function ${arrowFn[1] + params} ${fn}`
//     return console.log(regFn)
//   } else {
//     let regFnName = str.match(/\ (.*?)\(/)[1]
//     let params = str.match(/\((.*?)\)/)[0]
//     let fn = str.slice(str.indexOf('{'))
//     let arrowFn = `const ${regFnName} = ${params} => ${fn}`
//     return console.log(arrowFn)
//   }
// }

// convertFn('function(){}')

//------------------------------------------------------------
// const sampleArray = [1, 2, 3, 4, 3, 2, 1, 2, 5]

// const windowMaxes = (array, windowLength) => {
//   const maxNums = []
//   for (i = 0; i < array.length - windowLength + 1; i++) {
//     let maxNum = 0
//     console.log(i)
//     for (j = i; j < i + windowLength; j++) {
//       if (array[j] > maxNum) {
//         maxNum = array[j]
//       }
//     }
//     maxNums.push(maxNum)
//   }
//   return maxNums
// }

// console.log(windowMaxes(sampleArray, 3))

//----------------------------------------------

// const sampleArray = ['1a', 'a', '2b', 'b']

// const numInStr = (array) => {
//   const numsArray = []
//   const re = /(\d)/

//   array.forEach((string) => {
//     const isValid = re.test(string)
//     if (isValid) {
//       numsArray.push(string)
//     }
//   })

//   return numsArray
// }

// console.log(numInStr(sampleArray))

//------------------------------------------

// const additivePersistence = (num) => {
//   var count = 0

//   const recursion = (n) => {
//     const numToArray = n.toString().split('').map(Number)
//     if (numToArray.length === 1) {
//       return
//     } else {
//       count++
//       const totalNums = numToArray.reduce((a, b) => {
//         return a + b
//       })
//       recursion(totalNums)
//     }
//   }

//   recursion(num)

//   return count
// }

// console.log(additivePersistence(1679583))

//--------------------------------------------

// const f1 = (str) => {
//   const f2 = () => {
//     return str
//   }

//   return f2
// }

// const fn = f1('apple')

// console.log(fn())

//---------------------------------------------

// const isExactlyThree = (n) => {
//   let count = 0

//   for (i = 2; i <= n / 2; i++) {
//     if (count <= 1) {
//       if (n % i == 0) {
//         count += 1
//       }
//     } else {
//       return console.log('no')
//     }
//   }
//   if (count == 1) {
//     console.log('yes')
//   }
// }

// isExactlyThree(48)

//---------------------------------------------

// const sampleString = 'How the Avocado Became the Fruit of the Global Trade'

// const getHashTags = (string) => {
//   const array = string.split(' ').sort((a, b) => {
//     return b.length - a.length
//   })
//   const result = []
//   let i = 0
//   while (i < 3) {
//     if (array[i]) {
//       result.push('#' + array[i])
//     }
//     i++
//   }
//   return result
// }

// console.log(getHashTags(sampleString))
// console.log(
//   getHashTags(
//     'Why You Will Probably Pay More for Your Christmas Tree This Year'
//   )
// )
// console.log(getHashTags('Hey Parents, Surprise, Fruit Juice Is Not Fruit'))
// console.log(getHashTags('Visualizing Science'))

//------------------------------------------------------------------

// const sampleString = '3[a]2[c]'

// const stringBuilder = (string) => {
//   const regex = /(\d)\[([^\[\]]+)\]/
//   if (regex.test(string)) {
//     const match = regex.exec(string)
//     const newString = string.replace(regex, match[2].repeat(Number(match[1])))
//     return stringBuilder(newString)
//   } else {
//     return string
//   }
// }

// console.log(stringBuilder(sampleString))

//------------------------------------------------------------------

// const final = (r, c, k) => {
//   const matrix = []
//   for (i = 0; i < r; i++) {
//     const row = []
//     for (j = 0; j < c; j++) {
//       row.push(0)
//     }
//     matrix.push(row)
//   }

//   k.forEach((item) => {
//     regex = /(\d+)([cr])/g
//     const match = regex.exec(item)

//     if (match[2] === 'r') {
//       for (i = 0; i < c; i++) {
//         matrix[Number(match[1])][i] += 1
//       }
//     } else {
//       for (i = 0; i < r; i++) {
//         matrix[i][Number(match[1])] += 1
//       }
//     }
//   })

//   return matrix
// }

// console.log(final(3, 3, ['2r', '2c', '1r', '0c']).join('\n'))
// console.log(final(2, 2, ['0c']).join('\n'))
// console.log(final(3, 3, ['1c', '2c', '2c', '3c', '3c', '3c']).join('\n'))
// console.log(final(3, 3, []).join('\n'))

//---------------------------------------------------------

// function syllable(word) {
//   return word.split(/(?=[^aeiouy][aeiouy])(?!.e$)/)
// }

// console.log(syllable('pancake'))

//----------------------------------------------------

// const lcm = (arrayNums) => {
//   let highestNum = arrayNums.sort((a, b) => a - b)[arrayNums.length - 1]

//   if (
//     arrayNums.every((x) => {
//       return highestNum % x == 0
//     })
//   ) {
//     return highestNum
//   } else {
//     for (i = 2; i > 0; i++) {
//       if (
//         arrayNums.every((x) => {
//           return (highestNum * i) % x == 0
//         })
//       ) {
//         return highestNum * i
//       }
//     }
//   }
// }
// console.log(lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]))
// console.log(lcm([5, 7, 11, 35, 55, 77]))
// console.log(lcm([5]))
// console.log(lcm([5, 7, 11]))

//------------------------------------------------------------

// const sampleArray = ['oven', 'envier', 'erase', 'serious']
// const s2 = ['move', 'over', 'very']
// const s3 = ['to', 'ops', 'psy', 'syllable']
// const s4 = ['aaa', 'bbb', 'ccc', 'ddd']

// const join = (array) => {
//   let joined = array[0]
//   let overlap = []

//   dance: for (i = 0; i < array.length - 1; i++) {
//     for (j = 0; j < array[i].length; j++) {
//       if (array[i + 1].indexOf(array[i].slice(j)) == 0) {
//         overlap.push(array[i].length - j)
//         joined += array[i + 1].slice(array[i].length - j)
//         continue dance
//       }
//     }
//     joined += array[i + 1]
//     overlap.push(0)
//   }

//   const result = [
//     joined,
//     overlap.sort((a, b) => {
//       return a - b
//     })[0],
//   ]
//   return result
// }
// console.log(join(sampleArray))
// console.log(join(s2))
// console.log(join(s3))
// console.log(join(s4))

//----------------------------------------------------------------

// const distance = (str) => {
//   const arrayStr = str.split('')
//   const vowels = ['a', 'e', 'i', 'o', 'u']
//   const posVowels = []
//   const result = []

//   dance: for (i = 0; i < arrayStr.length; i++) {
//     for (j = 0; j < vowels.length; j++) {
//       if (arrayStr[i] == vowels[j]) {
//         posVowels.push(i)
//         continue dance
//       }
//     }
//   }

//   for (i = 0; i < arrayStr.length; i++) {
//     let count = []
//     for (j = 0; j < posVowels.length; j++) {
//       count.push(Math.abs(i - posVowels[j]))
//     }
//     result.push(
//       count.sort((a, b) => {
//         return a - b
//       })[0]
//     )
//   }

//   return result
// }

// distance('aaaaa')
// distance('babbb')
// distance('abcdabcd')
// distance('shopper')

//---------------------------------------------------------

// const m1 = [
//   [1, 2, 3],
//   [4, 5, 6],
//   [7, 8, 9],
// ]

// const m2 = [
//   [5, 1, 9, 11],
//   [2, 4, 8, 10],
//   [13, 3, 6, 7],
//   [15, 14, 12, 16],
// ]

// const rotate = (matrix) => {
//   for (i = matrix.length - 1; i >= 0; i--) {
//     dance: for (j = 0; j < matrix.length; j++) {
//       matrix[j].push(matrix[i].shift())
//       continue dance
//     }
//   }
// }

// console.log(m1)
// rotate(m1)
// console.log(m1)
// console.log(rotate(m2))
// console.log(rotate([[1]]))

//-----------------------------------------------------------------------

// const longestCommonPrefix = (array) => {
//   const sorted = array.sort((a, b) => {
//     return a.length - b.length
//   })

//   for (i = sorted[0].length; i > 0; i--) {
//     if (
//       sorted.every((item) => {
//         return item.indexOf(array[0].slice(0, i)) == 0
//       })
//     ) {
//       return array[0].slice(0, i)
//     }
//   }
//   return ''
// }

// longestCommonPrefix(['flower', 'flow', 'flight'])

//----------------------------------------------------------------------------

// const checkPattern = (array, string) => {
//   const arrayStr = string.split('')
//   const unique = new Set(arrayStr)
//   const dupPos = []

//   unique.forEach((item) => {
//     let count = []
//     for (j = 0; j < arrayStr.length; j++) {
//       if (item == arrayStr[j]) {
//         count.push(j)
//       }
//     }
//     dupPos.push(count)
//   })

//   let result = true

//   dupPos.forEach((item) => {
//     for (i = 0; i < item.length; i++) {
//       let array1 = array[item[0]]
//       let array2 = array[item[i]]

//       let isValid = array1.every(function (element, index) {
//         return element === array2[index]
//       })

//       if (isValid === false) {
//         result = false
//         return
//       }
//     }
//   })

//   return result
// }

// console.log(
//   checkPattern(
//     [
//       [1, 1],
//       [2, 2],
//       [1, 1],
//       [2, 2],
//     ],
//     'ABAB'
//   )
// )
// console.log(
//   checkPattern(
//     [
//       [1, 2],
//       [1, 3],
//       [1, 4],
//       [1, 2],
//     ],
//     'ABCA'
//   )
// )

// console.log(
//   checkPattern(
//     [
//       [1, 2],
//       [1, 2],
//       [1, 2],
//       [1, 2],
//     ],
//     'AABA'
//   )
// )

//------------------------------------------------------------------

// function checkPattern(arr, pattern) {
//   var dict = {}
//   for (var i in pattern) {
//     if (dict[pattern[i]]) {
//       if (dict[pattern[i]].join(',') != arr[i].join(',')) {
//         return false
//       }
//     } else {
//       dict[pattern[i]] = arr[i]
//     }
//   }
//   for (var i in dict) {
//     for (var j in dict) {
//       if (i != j && dict[i].join(',') == dict[j].join(',')) {
//         return false
//       }
//     }
//   }
//   return true
// }

// const a1 = [
//   [11, 2],
//   [1, 12],
//   [2, 2],
// ]

// console.log(checkPattern(a1, 'AAB'))

//------------------------------------------------------------------------

// const isConsecutive = (num) => {
//   dance: for (i = 1; i <= num.length / 2; i++) {
//     if (num.length % i == 0) {
//       let re = new RegExp(`.{1,${i}}`, 'g')
//       let numSplit = num.match(re)
//       console.log(numSplit)

//       for (j = 0; j < numSplit.length - 1; j++) {
//         if (Math.abs(Number(numSplit[j]) - Number(numSplit[j + 1])) !== 1) {
//           continue dance
//         }
//       }
//       return true
//     }
//   }

//   return false
// }

// console.log(isConsecutive('131618225055'))
// console.log(isConsecutive('123124125'))
// console.log(isConsecutive('32332432536'))
// console.log(isConsecutive('326325324323'))
// console.log(isConsecutive('667666'))
// console.log(isConsecutive('999897959493'))
// console.log(isConsecutive('273274273274'))

//-----------------------------------------------------------------

// const words = [
//   'a',
//   'after',
//   'all',
//   'an',
//   'and',
//   'are',
//   'as',
//   'by',
//   'continued',
//   'deadlines',
//   'doubly',
//   'fish',
//   'for',
//   'go',
//   'happen',
//   'happened',
//   'i',
//   'illusion',
//   'is',
//   'long',
//   'love',
//   'lunchtime',
//   'make',
//   'moment',
//   'noise',
//   'nothing',
//   'of',
//   'or',
//   'people',
//   'problem',
//   'second',
//   'so',
//   'summarize',
//   'summary',
//   'thanks',
//   'the',
//   'then',
//   'they',
//   'time',
//   'to',
//   'whooshing',
// ]

// const cleave = (str, words) => {
//   let j = 0
//   let result = []
//   dance: for (i = 0; i <= str.length; i++) {
//     const slice = str.slice(j, i)
//     for (k = 0; k < words.length; k++) {
//       if (
//         slice ==
//         words.sort((a, b) => {
//           return b.length - a.length
//         })[k]
//       ) {
//         j = i
//         result.push(slice)
//         continue dance
//       }
//     }
//   }
//   if (result.join('').length !== str.length) {
//     return 'Cleaving stalled: Word not found'
//   } else {
//     return result
//   }
// }

// console.log(
//   words.sort((a, b) => {
//     return b.length - a.length
//   })
// )
// const cleave = (str, words) => {
//   const separator = '_'

//   words
//     .sort((a, b) => b.length - a.length)
//     .forEach((word, i) => {
//       str = str.replace(new RegExp(word, 'g'), `${i}${separator}`)
//     })

//   console.log(str)
//   return /[a-z]/i.test(str)
//     ? 'Cleaving stalled: Word not found'
//     : str
//         .slice(0, -1)
//         .split(separator)
//         .map((i) => words[i])
//         .join(' ')
// }

// console.log(cleave('solongandthanksforallthefish', words))

//-----------------------------------------------------

// function flatten(r) {
//   const arr = []
//   for (const x of r) arr.push(...(Array.isArray(x) ? flatten(x) : [x]))
//   return arr
// }

// console.log(flatten([['hello1', ['hello5']], 'hello2', ['hello3']]))

//-----------------------------------------------------

// const modulo = (num1, num2) => {
//   let result = Math.abs(num1) - Math.abs(num2)
//   switch (true) {
//     case result < 0:
//       return num1
//     case result === 0:
//       return 0
//     default:
//       if (num1 < 0) {
//         return modulo(-result, num2)
//       } else {
//         return modulo(result, num2)
//       }
//   }
// }

// console.log(modulo(-51, -4))

// console.log(modulo(1024, 7))

// ----------------------------------------------------

// const invert = (arr) => {
//   let result = []

//   for (i in arr) {
//     let arr1 = []
//     for (j in arr[i]) {
//       let arr2 = []
//       for (k in arr[i][j]) {
//         var color = 255 - arr[i][j][k]
//         switch (true) {
//           case color > 255:
//             arr2.push(255)
//             break
//           case color < 0:
//             arr2.push(0)
//             break
//           default:
//             arr2.push(color)
//             break
//         }
//       }
//       arr1.push(arr2)
//     }
//     result.push(arr1)
//   }
//   return result
// }

// console.log(
//   invert([
//     [
//       [255, 255, 255],
//       [255, 255, 255],
//     ],
//     [
//       [255, 255, 255],
//       [255, 255, 255],
//     ],
//   ])
// )

// console.log(
//   invert([
//     [
//       [0, 0, 255],
//       [0, 0, 0],
//       [0, 0, 157],
//       [100, 229, 4],
//     ],
//     [
//       [100, 0, 3],
//       [1, 100, 0],
//       [0, 10, 0],
//       [0, 168, 0],
//     ],
//     [
//       [16, 30, 0],
//       [0, 125, 0],
//       [15, 0, 9],
//       [0, 139, 0],
//     ],
//     [
//       [200, 2, 0],
//       [0, 125, 0],
//       [0, 0, 9],
//       [0, 200, 0],
//     ],
//   ])
// )

// console.log(
//   invert([
//     [
//       [0, 255, 255],
//       [256, 255, 255],
//     ],
//     [
//       [255, -1, 255],
//       [255, 255, 255],
//     ],
//   ]),
//   [
//     [
//       [255, 0, 0],
//       [0, 0, 0],
//     ],
//     [
//       [0, 255, 0],
//       [0, 0, 0],
//     ],
//   ]
// )

//--------------------------------------------------

// const pokerHandRanking = (hand) => {
//   const cardNums = []
//   const suits = []

//   for (i in hand) {
//     cardNums.push(hand[i].slice(0, -1))
//     suits.push(hand[i].slice(-1))
//   }

//   let isRoyalFlush = () => {}
//   // if(cardNums.sort() == )

// }

// // pokerHandRanking(['10h', 'Jh', 'Qh', 'Ah', 'Kh'])

// const test1 = () => {
//   return true
// }

// const test2 = () => {
//   console.log('test2 ran')
//   return ''
// }

// const test = () => test1() && test2() && 'Royal Flush'

// const a = test1() && test2() && 'Royal Flush'
// console.log(a)

// ----------------------------------------------------

// const longest_substring = (str) => {
//   let realResult = []
//   for (j = 0; j < str.length; j++) {
//     let result = []

//     for (i = j; i < str.length; i++) {
//       const isValid = result.every((item) => {
//         return item !== str[i]
//       })

//       if (isValid) {
//         result.push(str[i])
//       } else {
//         realResult.push(result.length)
//         break
//       }
//       realResult.push(result.length)
//     }
//   }

//   if (str !== '') {
//     return realResult.sort((a, b) => {
//       return b - a
//     })[0]
//   } else {
//     return 0
//   }
// }

// console.log(longest_substring(' '))

// --------------------------------------------------------

// const sampleArray = [
//   { brand: 'NARS', name: 'Cosmetics Voyageur Pallete' },
//   { brand: 'NARS', name: 'Cosmetics Voyageur Pallete' },
//   { brand: 'Urban Decay', name: 'Naked Honey Pallete' },
//   { brand: 'Stila', name: 'Stay All Day Liquid Lipstick' },
//   { brand: 'Stila', name: 'Stay All Day Liquid Lipstick' },
//   { brand: 'Stila', name: 'Stay All Day Liquid Lipstick' },
// ]

// const simplify = (arr) => {
//   let result = []
//   for (i in arr) {
//     const isInResult = result.every((item) => {
//       return item.brand !== arr[i].brand && item.name !== arr[i].name
//     })
//     if (isInResult) {
//       result.push({ ...arr[i], count: 1 })
//     } else {
//       const objectIndex = result.findIndex((item) => {
//         return item.brand === arr[i].brand && item.name === arr[i].name
//       })

//       result[objectIndex].count += 1
//     }
//   }

//   return result
// }

// simplify(sampleArray)

// ----------------------------------------------------------------

// const isPalindrome = (string) => {
//   const specialChar = /([^A-Z a-z])/g
//   const whitespace = /\s+/g

//   const newString = string
//     .replace(specialChar, '')
//     .replace(whitespace, '')
//     .toLowerCase()

//   switch (true) {
//     case string.length == 1:
//       return true
//     case newString[0] !== newString[newString.length - 1]:
//       return false
//     case newString[0] == newString[newString.length - 1] &&
//       newString.length == 2:
//       return true
//     default:
//       return isPalindrome(newString.slice(1, newString.length - 1))
//   }
// }

// console.log(isPalindrome('Step on no pets!'))

// -------------------------------------------------------------------

// const numThenChar = (arr) => {
//   const numChar = arr.reduce((a, b) => {
//     return a.concat(b)
//   })

//   const nums = []
//   const chars = []

//   for (i in numChar) {
//     if (typeof numChar[i] === 'number') {
//       nums.push(numChar[i])
//     } else {
//       chars.push(numChar[i])
//     }
//   }

//   let sortedNumChar = nums
//     .sort((a, b) => {
//       return a - b
//     })
//     .concat(chars.sort())

//   let result = []

//   for (i in arr) {
//     let subresult = []
//     for (j in arr[i]) {
//       subresult.push(sortedNumChar.shift())
//     }
//     result.push(subresult)
//   }

//   return result
// }

// numThenChar([
//   [1, 2, 4, 3, 'a', 'b'],
//   [6, 'c', 5],
//   [7, 'd'],
//   ['f', 'e', 8],
// ])

// -------------------------------------------------------------

// const resist = (net) => {
//   const re = /\[([^\[\]\(\)]+)\]|\(([^\[\]\(\)]+)\)/

//   const match = net.match(re)

//   let result = 0

//   switch (true) {
//     case match == null:
//       return parseFloat(Number(net).toFixed(1))
//     case match[0][0] == '(':
//       result += JSON.parse(`[${match[2]}]`).reduce((acc, num) => {
//         return (acc += num)
//       })
//       break
//     case match[0][0] == '[':
//       result +=
//         1 /
//         JSON.parse(`${match[0]}`).reduce((acc, num) => {
//           return (acc += 1 / num)
//         }, 0)
//       break
//   }

//   return resist(net.replace(re, result.toString()))
// }
// console.log(resist('(10, [20, 30])'))
// console.log(resist('[10, (20, 30)]'))

// ----------------------------------------------------------

// const sample = [-1, -9, 0, 8, -76, 5, 3]

// const maxSum = (arrNums) => {
//   let count = 0
//   for (i = 0; i < arrNums.length; i++) {
//     for (j = i + 1; j <= arrNums.length; j++) {
//       var checkNum = arrNums.slice(i, j).reduce((a, b) => {
//         return (a += b)
//       })
//       if (checkNum > count) {
//         count = checkNum
//       }
//     }
//   }

//   return count
// }

// console.log(maxSum(sample))

// --------------------------------------------------------

// const polybius = (text) => {
//   const cipher = [
//     ['a', 'b', 'c', 'd', 'e'],
//     ['f', 'g', 'h', 'i', 'k'],
//     ['l', 'm', 'n', 'o', 'p'],
//     ['q', 'r', 's', 't', 'u'],
//     ['v', 'w', 'x', 'y', 'z'],
//   ]
//   let result = ''

//   const isNum = /^[\d\s]+$/.test(text)

//   if (isNum) {
//     const splitNums = [...text.matchAll(/[\d].|\s+/g)]

//     for (i in splitNums) {
//       var row = Number(splitNums[i][0].split('')[0])
//       var col = Number(splitNums[i][0].split('')[1])
//       if (row !== 0) {
//         result += cipher[row - 1][col - 1]
//       } else {
//         result += splitNums[i][0]
//       }
//     }
//   } else {
//     const newText = text.toLowerCase().replace(/j/g, 'i')
//     dance: for (i in newText) {
//       for (j in cipher) {
//         for (k in cipher[j]) {
//           if (newText[i].toLowerCase() === cipher[j][k]) {
//             var row = Number(j) + 1
//             var col = Number(k) + 1
//             result += row.toString() + col.toString()
//             continue dance
//           }
//         }
//       }
//       if (newText[i] == ' ') {
//         result += ' '
//       }
//     }
//   }

//   return result
// }

// console.log(
//   polybius('just because i dont care doesnt mean that i dont understand')
// )

// Disregard punctuation, but keep spaces - Expected: '24454344 12151311454315 24 14343344 13114215 143415433344 32151133 44231144 24 14343344 45331415424344113314', instead got: '454344 12151311454315 24 14343344 13114215 143415433344 32151133 44231144 24 14343344 45331415424344113314'

// -----------------------------------------------------------------------

// const classifyRug = (rug) => {
//   const isHorizontalSymmetric = () => {
//     let result = true
//     for (i = 0; i < Math.floor(rug.length / 2); i++) {
//       let j = rug.length - 1 - i

//       const isValid = rug[i].every((char, index) => {
//         return char == rug[j][index]
//       })

//       if (!isValid) {
//         result = false
//         break
//       }
//     }
//     return result
//   }

//   const isVerticalSymetric = () => {
//     let result = true
//     for (i = 0; i < rug.length; i++) {
//       for (j = 0; j <= Math.floor(rug[i].length / 2); j++) {
//         let k = rug[i].length - 1 - j
//         if (rug[i][j] !== rug[i][k]) {
//           result = false
//           break
//         }
//       }
//     }
//     return result
//   }

//   switch (true) {
//     case isVerticalSymetric() && isHorizontalSymmetric():
//       return 'perfect'
//     case isHorizontalSymmetric():
//       return 'horizontally symmetric'
//     case isVerticalSymetric():
//       return 'vertically symmetric'
//     default:
//       return 'imperfect'
//   }
// }

// const sample = [
//   ['a', 'b', 'a'],
//   ['b', 'b', 'b'],
//   ['a', 'b', 'a'],
//   ['a', 'b', 'a'],
// ]

// const sample2 = [
//   ['a', 'a', 'b'],
//   ['a', 'a', 'a'],
//   ['b', 'a', 'a'],
// ]
// console.log(classifyRug(sample2))

// ---------------------------------------------------------

// const convert = (s, numRows) => {
//   if (numRows == 1) {
//     return s
//   }
//   let result = []
//   for (i = 0; i < numRows; i++) {
//     result[i] = []
//   }
//   count = 0
//   countup = true
//   for (i = 0; i < s.length; i++) {
//     if (countup) {
//       result[count].push(s[i])
//       count++
//       if (count == numRows - 1) {
//         countup = false
//       }
//     } else {
//       result[count].push(s[i])
//       count--
//       if (count == 0) {
//         countup = true
//       }
//     }
//   }

//   return result.flat().join('')
// }

// console.log(convert('PAYPALISHIRING', 1))

// -----------------------------------------------------------

// const sampleObject = {
//   0: { age: 18, name: 'john', marks: '400' },
//   1: { age: 17, name: 'julie', marks: '400' },
//   2: { age: 16, name: 'Robin', marks: '200' },
//   3: { age: 16, name: 'Bella', marks: '300' },
//   4: { age: 16, name: 'john', marks: '250' },
//   5: { age: 15, name: 'julie', marks: '250' },
// }

// const getObject = (obj) => {
//   const result = {}
//   let count = 0
//   dance: for (x in obj) {
//     for (y in result) {
//       if (obj[x].marks == result[y].marks) {
//         if (obj[x].age > result[y].age) {
//           result[y].name = obj[x].name
//           result[y].age = obj[x].age
//         }
//         continue dance
//       }
//     }
//     result[count] = obj[x]
//     count += 1
//   }

//   return result
// }

// getObject(sampleObject)

// -------------------------------------------------------

// const makeBox = (num) => {
//   let result = []

//   for (i = 0; i < num; i++) {
//     let subResult = ''
//     if (i == 0 || i == num - 1) {
//       subResult += '#'.repeat(num)
//       console.log(subResult)
//     } else {
//       subResult += '#' + ' '.repeat(num - 2) + '#'
//     }
//     result.push(subResult)
//   }
//   return result
// }

// console.log(makeBox(5))

// -------------------------------------------------------

// const majorityVote = (votes) => {
//   let result = {}
//   for (i in votes) {
//     if (!result[votes[i]]) {
//       result[votes[i]] = 1
//     } else {
//       result[votes[i]] += 1
//     }
//   }

//   for (x in result) {
//     if (result[x] > votes.length / 2) {
//       return x
//     }
//   }
//   return null
// }

// console.log(majorityVote([]))

// --------------------------------------------------------

// const maxPossible = (num1, num2) => {
//   const n1 = num1
//     .toString()
//     .split('')
//     .map((item) => {
//       return Number(item)
//     })

//   const n2 = num2
//     .toString()
//     .split('')
//     .map((item) => {
//       return Number(item)
//     })
//     .sort((a, b) => {
//       return b - a
//     })

//   for (i in n1) {
//     if (n2[0] > n1[i]) {
//       n1[i] = n2.shift()
//     }
//   }

//   return Number(n1.join(''))
// }

// maxPossible(9132, 5564)
// maxPossible(8732, 91255)

// ------------------------------------------------------------

// const minPalindromeSteps = (string) => {
//   for (i = 0; i < string.length; i++) {
//     let isMiniPalindrome = true
//     if (string[string.length - 1] == string[i]) {
//       let k = 0
//       for (j = i; j < string.length; j++) {
//         if (string[j] !== string[string.length - 1 - k]) {
//           isMiniPalindrome = false
//         }
//         k++
//       }
//     } else {
//       isMiniPalindrome = false
//     }

//     if (isMiniPalindrome) {
//       return i
//     }
//   }
// }

// // console.log(minPalindromeSteps('race'))
// console.log(minPalindromeSteps('mada'))
// console.log(minPalindromeSteps('racecar'))

// ------------------------------------------------------------

// sampleRoads = {
//   graph: {
//     directed: false,
//     nodes: [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }, { id: 4 }],
//     edges: [
//       {
//         source: 0,
//         target: 1,
//         metadata: {
//           distance: 5,
//         },
//       },
//       {
//         source: 1,
//         target: 3,
//         metadata: {
//           distance: 9,
//         },
//       },
//       {
//         source: 3,
//         target: 2,
//         metadata: {
//           distance: 6,
//         },
//       },
//       {
//         source: 2,
//         target: 4,
//         metadata: {
//           distance: 3,
//         },
//       },
//       {
//         source: 4,
//         target: 3,
//         metadata: {
//           distance: 8,
//         },
//       },
//       {
//         source: 4,
//         target: 0,
//         metadata: {
//           distance: 2,
//         },
//       },
//     ],
//   },
// }

// const sampleRoads = {
//   graph: {
//     directed: false,
//     nodes: [
//       { id: 0 },
//       { id: 1 },
//       { id: 2 },
//       { id: 3 },
//       { id: 4 },
//       { id: 5 },
//       { id: 6 },
//       { id: 7 },
//       { id: 8 },
//       { id: 9 },
//     ],
//     edges: [
//       {
//         source: 1,
//         target: 6,
//         label: 'Oak Street',
//         metadata: {
//           distance: 5,
//         },
//       },
//       {
//         source: 6,
//         target: 8,
//         label: 'Oak Street',
//         metadata: {
//           distance: 6,
//         },
//       },
//       {
//         source: 8,
//         target: 9,
//         label: 'Oak Street',
//         metadata: {
//           distance: 11,
//         },
//       },
//       {
//         source: 8,
//         target: 7,
//         label: 'Robin Way',
//         metadata: {
//           distance: 3,
//         },
//       },
//       {
//         source: 7,
//         target: 4,
//         label: 'Robin Way',
//         metadata: {
//           distance: 5,
//         },
//       },
//       {
//         source: 6,
//         target: 7,
//         label: 'Mountain Road',
//         metadata: {
//           distance: 8,
//         },
//       },
//       {
//         source: 7,
//         target: 9,
//         label: 'Mountain Road',
//         metadata: {
//           distance: 9,
//         },
//       },
//       {
//         source: 4,
//         target: 3,
//         label: 'National Street',
//         metadata: {
//           distance: 6,
//         },
//       },
//       {
//         source: 1,
//         target: 0,
//         label: 'Sunrise Drive',
//         metadata: {
//           distance: 4,
//         },
//       },
//       {
//         source: 0,
//         target: 3,
//         label: 'Short Street',
//         metadata: {
//           distance: 3,
//         },
//       },
//       {
//         source: 5,
//         target: 4,
//         label: 'Rickety Creek',
//         metadata: {
//           distance: 7,
//         },
//       },
//       {
//         source: 4,
//         target: 0,
//         label: 'Rickety Creek',
//         metadata: {
//           distance: 5,
//         },
//       },
//       {
//         source: 9,
//         target: 5,
//         label: 'Uphill Grove',
//         metadata: {
//           distance: 6,
//         },
//       },
//       {
//         source: 5,
//         target: 2,
//         label: 'Uphill Grove',
//         metadata: {
//           distance: 5,
//         },
//       },
//       {
//         source: 2,
//         target: 3,
//         label: 'Uphill Grove',
//         metadata: {
//           distance: 7,
//         },
//       },
//     ],
//   },
// }

// const navigator = (road, start, end) => {
//   const { edges } = road.graph
//   const { nodes } = road.graph
//   var table = {}
//   var visited = []
//   var unvisited = []

//   // Populate unvisited nodes
//   for (x in nodes) {
//     unvisited.push(nodes[x].id)
//   }

//   // Populate Table
//   for (i in nodes) {
//     table[nodes[i].id] = { shortestDistance: Infinity, path: null }
//   }

//   // Instantiate starting node distance as 0
//   table[start].shortestDistance = 0

//   // Visit neighbouring nodes
//   while (unvisited.length > 0) {
//     // Get node with shortest distance
//     var currentNode = Object.keys(table)
//       .filter((x) => {
//         for (a in unvisited) {
//           if (x == unvisited[a]) {
//             return true
//           }
//         }
//       })
//       .sort((a, b) => {
//         return table[a].shortestDistance - table[b].shortestDistance
//       })[0]

//     for (q in edges) {
//       var dist =
//         table[currentNode].shortestDistance + edges[q].metadata.distance

//       //If source/target match current node and corresponding source/target distance + current node shortest distance is less than target/source shortest distance in the table then add to table
//       if (
//         edges[q].source == currentNode &&
//         dist < table[edges[q].target].shortestDistance
//       ) {
//         table[edges[q].target].shortestDistance = dist
//         table[edges[q].target].path = currentNode
//       } else if (
//         edges[q].target == currentNode &&
//         dist < table[edges[q].source].shortestDistance
//       ) {
//         table[edges[q].source].shortestDistance = dist
//         table[edges[q].source].path = currentNode
//       }
//     }

//     visited.push(currentNode)

//     unvisited.splice(
//       unvisited.findIndex((id) => {
//         return id == currentNode
//       }),
//       1
//     )
//   }

//   //We use the visited array to determine the path taken.
//   //Shortets path taken = everything before the its position within the visited array
//   //For the starting point, this would be null

//   var path = [end]
//   for (i in Object.keys(table)) {
//     if (path[0] == start) {
//       break
//     } else {
//       path.unshift(table[path[0]].path)
//     }
//   }

//   return {
//     distance: Number(table[end].shortestDistance),
//     path: path.map((z) => {
//       return Number(z)
//     }),
//   }
// }

// console.log(navigator(sampleRoads, 6, 2))

//--------------------------------------------------------------

// const largestIsland = (map) => {
//   let visitedNodes = []
//   let result = []
//   let count = 0

//   const adj = ([x, y]) => {
//     let adjNodes = []
//     for (i = -1; i <= 1; i++) {
//       for (j = -1; j <= 1; j++) {
//         if (
//           x + i < map.length &&
//           x + i >= 0 &&
//           y + j < map[x].length &&
//           y + j >= 0 &&
//           map[x + i][y + j] == 1
//         ) {
//           adjNodes.push([x + i, y + j])
//         }
//       }
//     }

//     return adjNodes
//   }

//   const dfs = (node) => {
//     let adjacentNodes = adj(node)
//     let visited = visitedNodes.some((a) => {
//       return a.every((b, index) => {
//         return b == [node[0], node[1]][index]
//       })
//     })

//     if (visited) {
//       return
//     } else {
//       count += 1
//       visitedNodes.push(node)
//       for (x in adjacentNodes) {
//         dfs(adjacentNodes[x])
//       }
//     }
//   }

//   for (i in map) {
//     for (j in map[i]) {
//       var currentNode = [Number(i), Number(j)]
//       //Check if [i, j] is in visitedNodes
//       var isVisited = visitedNodes.some((a) => {
//         return a.every((b, index) => {
//           return b == [i, j][index]
//         })
//       })

//       //Find unvisited nodes
//       if (map[i][j] == 1 && !isVisited) {
//         //Run DFS
//         dfs(currentNode)
//         result.push(count)
//         count = 0
//       }
//     }
//   }

//   return result.sort((a, b) => {
//     return b - a
//   })[0]
// }

// const map1 = [
//   [0, 1, 0],
//   [0, 1, 1],
//   [0, 1, 1],
// ]

// const map2 = [
//   [1, 0, 0],
//   [0, 0, 0],
//   [0, 0, 1],
// ]

// const map3 = [
//   [1, 0, 0],
//   [1, 0, 0],
//   [1, 0, 1],
// ]

// const map4 = [
//   [1, 0, 0, 0],
//   [1, 0, 0, 1],
//   [1, 0, 1, 1],
//   [1, 0, 1, 1],
//   [1, 0, 1, 1],
// ]

// const map5 = [
//   [1, 0, 0, 0],
//   [1, 0, 0, 1],
//   [1, 0, 1, 1],
//   [1, 0, 0, 1],
//   [1, 0, 1, 1],
//   [1, 0, 0, 0],
//   [1, 0, 0, 1],
//   [1, 0, 1, 1],
//   [1, 0, 0, 1],
//   [1, 0, 1, 1],
// ]
// console.log(largestIsland(map5))
// largestIsland(map2)
// largestIsland(map3)
// largestIsland(map4)

// --------------------------------------------------------------------

// const threeSum = (nums) => {
//   let result = []
//   for (i = 0; i < nums.length; i++) {
//     for (j = i + 1; j < nums.length - 1; j++) {
//       if (nums[i] + nums[i + 1] + nums[j] == 0) {
//         result.push([nums[i], nums[i + 1], nums[j]])
//       }
//     }
//   }

//   return result
// }

// const threeSum = (nums) => {
//   let result = []

//   const sortNums = nums.sort((a, b) => {
//     return a - b
//   })

//   for (i = 0; i < sortNums.length; i++) {
//     if (i > 0 && sortNums[i] == sortNums[i - 1]) {
//       continue
//     }

//     var left = i + 1
//     var right = nums.length - 1

//     while (left < right) {
//       let threeSum = sortNums[i] + sortNums[left] + sortNums[right]

//       if (threeSum > 0) {
//         right -= 1
//       } else if (threeSum < 0) {
//         left += 1
//       } else {
//         result.push([sortNums[i], sortNums[left], sortNums[right]])
//         left += 1
//         while (sortNums[left] == sortNums[left - 1] && left < right) {
//           left += 1
//         }
//       }
//     }
//   }

//   return result
// }

// console.log(threeSum([-1, 0, 1, 2, -1, -4]))
// console.log(threeSum([0, 0, 0, 0]))

// ---------------------------------------------------------

// // don't change this code
// class Node {
//   constructor(v) {
//     this.val = v
//     this.next = null
//   }
// }
// class LinkedList {
//   constructor(a) {
//     this.head = null
//     this.tail = null
//     if (!!a) {
//       a.forEach((v) => {
//         this.insertTail(v)
//       })
//     }
//   }
//   insertHead(v) {
//     let nn = new Node(v)
//     nn.next = this.head
//     if (!this.tail) {
//       this.tail = nn
//     }
//     this.head = nn
//   }
//   insertTail(v) {
//     if (!this.head) return this.insertHead(v)
//     let nn = new Node(v)
//     this.tail.next = nn
//     this.tail = nn
//   }
//   print() {
//     let o = [],
//       node = this.head
//     while (node) {
//       o.push(node.val)
//       node = node.next
//     }
//     return o
//   }
// }
// // okay, you can change stuff below this line. Have fun!

// const list1 = new LinkedList([1, 2, 3, 4, 5, 6])
// const list2 = new LinkedList([8, 6, 7, 5, 3, 0, 9])
// const list3 = new LinkedList([1, 1, 3, 8])
// const list4 = new LinkedList(['a', 'b', 'c', 'e'])
// const list5 = new LinkedList(['r', 'a', 'c', 'e', 'c', 'a', 'r'])
// const list6 = new LinkedList([1])

// const reverseLinkedList = (linkedlist) => {
//   var current = linkedlist.head
//   var next = null
//   var temp_next = linkedlist.head.next
//   while (true) {
//     current.next = next
//     // head.next = null | node2.next = head
//     next = current
//     // next = head |next = node2

//     if (temp_next == null) {
//       break
//     }
//     current = temp_next
//     // current = node2 | current = node3

//     temp_next = temp_next.next
//     // temp_next = node3 | temp_next = node4
//   }

//   ;[linkedlist.head, linkedlist.tail] = [linkedlist.tail, linkedlist.head]

//   return linkedlist.print()
// }

// console.log(reverseLinkedList(list6))
// console.log(list6)

// ------------------------------------------------------------------

// const products = [
//   { number: 1, price: 100, name: 'Orange juice' },
//   { number: 2, price: 200, name: 'Soda' },
//   { number: 3, price: 150, name: 'Chocolate snack' },
//   { number: 4, price: 250, name: 'Cookies' },
//   { number: 5, price: 180, name: 'Gummy bears' },
//   { number: 6, price: 500, name: 'Condoms' },
//   { number: 7, price: 120, name: 'Crackers' },
//   { number: 8, price: 220, name: 'Potato chips' },
//   { number: 9, price: 80, name: 'Small snack' },
// ]

// const vendingMachine = (products, money, code) => {
//   //Binary Search
//   let start = 0,
//     end = products.length - 1

//   let res

//   while (start <= end) {
//     let mid = Math.floor((start + end) / 2)
//     if (code == products[mid].number) {
//       res = mid
//       break
//     } else if (code > products[mid].number) {
//       start = mid + 1
//     } else {
//       end = mid - 1
//     }
//   }

//   console.log(res)
//   const coins = [500, 200, 100, 50, 20, 10]
//   if (res >= 0) {
//     if (products[res].price > money) {
//       return 'Not enough money for this product'
//     } else {
//       let change = []
//       let changeSum = money - products[res].price
//       while (changeSum > 0) {
//         for (i in coins) {
//           if (coins[i] <= changeSum) {
//             changeSum -= coins[i]
//             change.push(coins[i])
//             break
//           }
//         }
//       }
//       return {
//         product: products[res].name,
//         change: change.sort((a, b) => {
//           return b - a
//         }),
//       }
//     }
//   } else {
//     return 'Enter a valid product number'
//   }
// }

// console.log(vendingMachine(products, 100, 1))

// --------------------------------------------------------------

// const security = (txt) => {
//   let re = /T([^G$T]+)\$|\$([^G$T]+)T/g
//   let result = re.test(txt)

//   if (result) {
//     return 'ALARM!'
//   } else {
//     return 'Safe'
//   }
// }

// console.log(
//   security('xxxxTTxGxx$xxTxxx'),
//   security('xxTxxG$xxxx$xxxx'),
//   security('TTxxxx$xxGxx$Gxxx')
// )

// ----------------------------------------------------------

// const doubleSwap = (str, c1, c2) => {
//   var res = ''

//   for (i in str) {
//     switch (true) {
//       case str[i] == c1:
//         res += c2
//         break
//       case str[i] == c2:
//         res += c1
//         break
//       default:
//         res += str[i]
//     }
//   }

//   return res
// }

// console.log(
//   doubleSwap('aabbccc', 'a', 'b'),
//   doubleSwap('128 895 556 788 999', '8', '9'),
//   doubleSwap('random w#rds writt&n h&r&', '#', '&')
// )

// ------------------------------------------------------------

// let errorLog = {}

// let promise = new Promise((resolve, reject) => {
//   throw new Error('Something failed')
// }).catch((err) => {
//   return (errorLog = err)
// })

//You must return in order for the promise status == 'fulfilled' -- the test checks for this

// -------------------------------------------------------------

// const getSubsets = (nums, target) => {
//   return nums
//     .reduce((a, c) => a.concat(a.map((b) => [...b, c])), [[]])
//     .filter((x) => {
//       if (
//         x.reduce((a, b) => {
//           return a + b
//         }, 0) == target
//       ) {
//         return x
//       }
//     })
//     .sort((k, j) => {
//       if (k.length == j.length) {
//         for (i in k) {
//           if (k[i] - j[i] != 0) {
//             return k[i] - j[i]
//           }
//         }
//       } else {
//         return k.length - j.length
//       }
//     })
// }
// console.log(getSubsets([-1, 0, 1, 2], 2), getSubsets([1, 2, 3, 4], 5))

// ---------------------------------------------------------------

// const isWristband = (pattern) => {
//   const isHorizontal = (x) => {
//     return x.every((z) => {
//       return z.every((color) => {
//         return color == z[0]
//       })
//     })
//   }

//   const isVertical = (x) => {
//     console.log(x)
//     return x[0].every((a, index) => {
//       return x.every((b) => {
//         return b[index] == a
//       })
//     })
//   }

//   const isDiagonalRight = (q) => {
//     return q.every((w, index1) => {
//       if (index1 !== q.length - 1) {
//         var rotated = w.slice(1, w.length)
//         return rotated.every((m, n) => {
//           return q[index1 + 1][n] == m
//           // }
//         })
//       } else {
//         return true
//       }
//     })
//   }

//   const isDiagonalLeft = (p) => {
//     return p.every((a, index) => {
//       if (index !== p.length - 1) {
//         var rotated = a.slice(0, a.length - 1)
//         return rotated.every((m, n) => {
//           return p[index + 1][n + 1] == m
//         })
//       } else {
//         return true
//       }
//     })
//   }

//   let res = [
//     isDiagonalLeft(pattern),
//     isDiagonalRight(pattern),
//     isHorizontal(pattern),
//     isVertical(pattern),
//   ]
//   return res
// }

// // console.log(
// //   isWristband([
// //     ['A', 'B'],
// //     ['A', 'B'],
// //     ['A', 'B'],
// //   ])
// // )

// console.log(
//   isWristband([
//     ['A', 'B', 'C'],
//     ['C', 'A', 'B'],
//     ['B', 'C', 'A'],
//     ['A', 'B', 'C'],
//   ])
// )

// // Diagonal Right
// console.log(
//   isWristband([
//     ['A', 'B', 'C'],
//     ['B', 'C', 'A'],
//     ['C', 'A', 'B'],
//     ['A', 'B', 'A'],
//   ])
// )

// console.log(
//   isWristband([
//     ['A', 'B', 'C'],
//     ['B', 'C', 'D'],
//     ['C', 'D', 'E'],
//     ['D', 'E', 'E'],
//   ])
// )

// -------------------------------------------------------------------

// const groupAnagrams = (arr) => {
//   let result = []

//   while (arr.length > 0) {
//     let subResult = []

//     let j = 0
//     while (j < arr.length) {
//       let reverse = arr[0].split('').sort().join('')
//       let word = arr[j].split('').sort().join('')
//       if (j != 0 && word == reverse) {
//         subResult.push(arr.splice(j, 1)[0])
//         j -= 1
//       }
//       j += 1
//     }

//     subResult.push(arr.shift())

//     result.push(subResult)
//   }

//   return result
// }

// console.log(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
// console.log(groupAnagrams(['']))
// console.log(groupAnagrams([''])

// const groupAnagrams = (arr) => {
//   const hashMap = new Map()

//   for (i in arr) {
//     let sortStr = arr[i].split('').sort().join('')
//     if (hashMap.has(sortStr)) {
//       hashMap.set(sortStr, [...hashMap.get(sortStr), arr[i]])
//     } else {
//       hashMap.set(sortStr, [arr[i]])
//     }
//   }

//   return Array.from(hashMap.values())
// }

// console.log(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
// console.log(groupAnagrams(['']))
// console.log(groupAnagrams(['', '', '']))

// -------------------------------------------------------------------

// const findFrequent = (list) => {
//   const item = new Map()

//   for (i in list) {
//     if (item.has(list[i])) {
//       item.set(list[i], item.get(list[i]) + 1)
//     } else {
//       item.set(list[i], 1)
//     }
//   }

//   let res = []

//   for (x of item.entries()) {
//     res.push(x)
//   }
//   return res.sort((a, b) => {
//     return b[1] - a[1]
//   })[0][0]
// }

// console.log(findFrequent([3, 7, 3]))
// console.log(findFrequent([null, 'hello', true, null]))

// ---------------------------------------------------------------------

// class Battleship {
//   constructor(scheme, input) {
//     this.scheme = scheme
//     this.input = input
//     this.hit = 0
//     this.score = 0
//     this.sunkCruisers = 0
//     this.bo = this.buildboard()
//   }

//   buildboard() {
//     var bo = [
//       ['○', '○', '○', '○', '○'],
//       ['○', '○', '○', '○', '○'],
//       ['○', '○', '○', '○', '○'],
//       ['○', '○', '○', '○', '○'],
//       ['○', '○', '○', '○', '○'],
//     ]

//     for (var i in this.scheme) {
//       var y = this.scheme[i].charCodeAt(0) - 65
//       var x = Number(this.scheme[i][1]) - 1
//       bo[y][x] = '●'
//     }

//     for (var h in this.input) {
//       var y = this.input[h].charCodeAt(0) - 65
//       var x = Number(this.input[h][1]) - 1
//       if (bo[y][x] == '●') {
//         bo[y][x] = '☀'
//         this.hit += 1
//         this.score += 1
//       } else {
//         bo[y][x] = '☼'
//       }
//     }

//     for (var m in this.input) {
//       var y = this.input[m].charCodeAt(0) - 65
//       var x = Number(this.input[m][1]) - 1
//       if (bo[y][x] == '☀' && this.adj([x, y], bo)) {
//         this.sunkCruisers += 1 / 2
//         this.score += 1
//       }
//     }

//     return bo
//   }

//   adj(pos, bo) {
//     let x = pos[0]
//     let y = pos[1]
//     var left = x - 1 >= 0 ? bo[y][x - 1] : 0
//     var right = x + 1 < bo[y].length ? bo[y][x + 1] : 0
//     var bottom = y + 1 < bo.length ? bo[y + 1][x] : 0
//     var top = y - 1 >= 0 ? bo[y - 1][x] : 0

//     if (left == '☀' || right == '☀' || top == '☀' || bottom == '☀') {
//       return true
//     } else {
//       return false
//     }
//   }

//   board() {
//     return this.bo
//   }

//   hits() {
//     return this.hit
//   }

//   points() {
//     return this.score
//   }

//   sunk() {
//     return this.sunkCruisers
//   }
// }

// const s1 = ['A1', 'C1', 'B2', 'B3', 'D2', 'E2', 'E4', 'E5', 'A5']
// const input1 = ['A1', 'B2', 'C3', 'D4', 'E5', 'E4']
// const s2 = ['A1', 'C1', 'B2', 'B3', 'D2', 'E2', 'E4', 'E5', 'A5']
// const input2 = ['A1', 'B2', 'C3', 'D4', 'E5', 'E4']
// const s3 = ['A2', 'A4', 'C1', 'C2', 'E3', 'C4', 'C5', 'D3', 'E5']
// const input3 = ['A1', 'B1', 'D1', 'E1', 'A3', 'A4']
// const s4 = ['A1', 'B1', 'D1', 'E1', 'A3', 'A4', 'D3', 'E4', 'D5']
// const input4 = ['A2', 'B4', 'C1', 'D3', 'E5', 'A5']
// const b2 = new Battleship(s4, input3)
// const b3 = new Battleship(s1, input1)

// console.log(b2)
// console.log(b3)

// -------------------------------------------------------------------

// const snake = (n) => {
//   total = n * n

//   var count = 0
//   let snake = 1
//   while (true) {
//     snake *= 2
//     if (snake > total) {
//       break
//     }
//     count += 1
//   }

//   return count
// }

// console.log(snake(3), snake(6), snake(24))

// ------------------------------------------------------------------------------

// const scoreIt = (s) => {
//   res = 0

//   count = 0

//   num = ''

//   for (i in s) {
//     switch (true) {
//       case s[i] == '(':
//         res += Number(num) * count
//         num = ''
//         count += 1
//         break
//       case s[i] == ')':
//         res += Number(num) * count
//         num = ''
//         count -= 1
//         break
//       case !isNaN(s[i]):
//         num += s[i]
//     }
//   }

//   return res
// }

// console.log(scoreIt('4(123)'))

// ------------------------------------------------------------------

// const compareVersion = (version1, version2) => {
//   const v1 = version1.split('.')
//   const v2 = version2.split('.')

//   var sim1 = ''
//   var sim2 = ''

//   for (i in v1.length > v2.length ? v1 : v2) {
//     const rev1 = v1[i] ? Number(v1[i]) : 0
//     const rev2 = v2[i] ? Number(v2[i]) : 0

//     sim1 += String(rev1)
//     sim2 += String(rev2)
//   }

//   switch (true) {
//     case Number(sim1) > Number(sim2):
//       return 1
//     case Number(sim1) < Number(sim2):
//       return -1
//     default:
//       return 0
//   }
// }

// console.log(compareVersion('1.01', '1.001'))

// console.log(compareVersion('1.0', '1.0.0'))

// console.log(compareVersion('0.1', '1.1'))

// console.log(compareVersion('1.0.1', '1'))

// console.log(compareVersion('7.5.2.4', '7.5.3'))

// -------------------------------------------------------------

// function climbingStairs(cost) {
//   for (i = 2; i < cost.length; i++) {
//     cost[i] += Math.min(cost[i - 1], cost[i - 2])
//     console.log(cost)
//   }
//   return Math.min(...cost.slice(-2))
// }

// console.log(climbingStairs([1, 2, 3, 4, 1, 5, 6, 3, 8]))

// --------------------------------------------------------------

// const isLandPerimeter = (grid) => {
//   let count = 0
//   for (i = 0; i < grid.length; i++) {
//     for (m = 0; m < grid[i].length; m++) {
//       if (grid[i][m] == 1) {
//         // Check Left
//         if (m - 1 < 0) {
//           count += 1
//         } else if (grid[i][m - 1] == 0) {
//           count += 1
//         }

//         //Check Right
//         if (m + 1 > grid[i].length - 1) {
//           count += 1
//         } else if (grid[i][m + 1] == 0) {
//           count += 1
//         }

//         //Check top
//         if (i - 1 < 0) {
//           count += 1
//         } else if (grid[i - 1][m] == 0) {
//           count += 1
//         }

//         //Check Bottom
//         if (i + 1 > grid.length - 1) {
//           count += 1
//         } else if (grid[i + 1][m] == 0) {
//           count += 1
//         }
//       }
//     }
//   }
//   return count
// }

// console.log(
//   isLandPerimeter([
//     [0, 1, 0, 0],
//     [1, 1, 1, 0],
//     [0, 1, 0, 0],
//     [1, 1, 0, 0],
//   ])
// )

// ------------------------------------------------------------------

// const restoreIPaddress = (s) => {
//   //Backtracking
//   let res = []

//   let N = s.length

//   const backtrack = (temp, pos, dot) => {
//     console.log(temp, pos, dot)

//     if (pos > N) {
//       return
//     }

//     if (pos == N && dot == 4) {
//       res.push(temp)
//       return
//     }

//     if ((pos == N && dot < 4) || (pos < N && dot == 4)) {
//       return
//     }

//     if (s[pos] == '0') {
//       backtrack(temp.concat([s.slice(pos, pos + 1)]), pos + 1, dot + 1)
//       return
//     }

//     //trying 1, 2 and 3 numbers
//     backtrack(temp.concat([s.slice(pos, pos + 1)]), pos + 1, dot + 1)
//     backtrack(temp.concat([s.slice(pos, pos + 2)]), pos + 2, dot + 1)

//     if (Number(s.slice(pos, pos + 3)) <= 255) {
//       backtrack(temp.concat([s.slice(pos, pos + 3)]), pos + 3, dot + 1)
//     }
//   }

//   backtrack([], 0, 0)

//   return res
// }

// console.log(restoreIPaddress('25525511135'))

// --------------------------------------------------------

// const gridPos = (pos) => {
//   let combos = []

//   for (i = 0; i < pos[0]; i++) {
//     combos.push('Up')
//   }

//   for (x = 0; x < pos[1]; x++) {
//     combos.push('Left')
//   }

//   const permutations = combos.reduce(
//     (a, c) => a.concat(a.map((b) => [...b, c])),
//     [[]]
//   )

//   let result = []

//   const permute = (arr, m = []) => {
//     if (arr.length === 0) {
//       result.push(m)
//     } else {
//       for (let i = 0; i < arr.length; i++) {
//         let curr = arr.slice()
//         let next = curr.splice(i, 1)
//         permute(curr.slice(), m.concat(next))
//       }
//     }
//   }

//   permute(combos)

//   return combos.length
// }

// console.log(gridPos([1, 1]))

// ---------------------------------------------------------

// const gridPos = (pos) => {
//   const fact = (num, count = 1) => {
//     if (num == 0) {
//       return count
//     }

//     count *= num

//     return fact(num - 1, count)
//   }

//   return fact(pos[0] + pos[1]) / fact(pos[1]) / fact(pos[0])
// }

// console.log(gridPos([1, 1]))

// ---------------------------------------------------------

// const simple_increment = (n, iterations, step) => {
//   let pos = String(n).length - 1

//   while (iterations != 0) {
//     // Move pointer

//     let trans = step % String(n).length
//     pos =
//       pos - trans < 0 ? String(n).length - Math.abs(pos - trans) : pos - trans

//     n += 10 ** pos

//     iterations -= 1
//   }
//   return n
// }

// console.log(simple_increment(99, 99, 99))
// console.log(simple_increment(1673, 2, 16))

// -------------------------------------------------------------

// const findAndRemove = (obj) => {
//   for (const [key, value] of Object.entries(obj)) {
//     for (const [key2, value2] of Object.entries(value)) {
//       if (isNaN(value2)) {
//         delete obj[key][key2]
//       } else {
//         obj[key][key2] = Number(value2)
//       }
//     }
//   }

//   return obj
// }

// console.log(
//   findAndRemove({
//     kitchen: {
//       ['gold spoons']: '900',
//       piano: '550',
//       notes: 'ga0r76ba22g4e',
//     },
//     cellar: {
//       reminder: 'dog',
//       bottle: '750',
//     },
//   })
// )

// ----------------------------------------------------------
//Definition for singly-linked list.
// function ListNode(val, next) {
//   this.val = val === undefined ? 0 : val
//   this.next = next === undefined ? null : next
// }

// const addTwoNumbers = (n1, n2) => {
//   var num1 = []
//   var num2 = []

//   let node1 = n1
//   while (true) {
//     num1.push(String(node1.val))
//     if (node1.next == null) {
//       break
//     }
//     node1 = node1.next
//   }

//   let node2 = n2
//   while (true) {
//     num2.push(String(node2.val))
//     if (node2.next == null) {
//       break
//     }
//     node2 = node2.next
//   }

//   const sum = String(
//     Number(num1.reverse().join('')) + Number(num2.reverse().join(''))
//   ).split('')

//   let i = 0
//   let resNode = null
//   while (i < sum.length) {
//     newNode = new ListNode(Number(sum[i]), resNode)

//     resNode = newNode

//     i++
//   }

//   console.log(sum)

//   return resNode
// }

// l1 = [2, 4, 3]
// l2 = [5, 6, 4]

//  Definition for singly-linked list.
// function ListNode(val, next) {
//   this.val = val === undefined ? 0 : val
//   this.next = next === undefined ? null : next
// }

// const addTwoNumber = (l1, l2) => {
//   var n1 = l1
//   var n2 = l2
//   let node = new ListNode()
//   const start = node
//   while (true) {
//     if (!n1 && !n2) {
//       return start
//     }
//     var val1 = !n1 ? 0 : n1.val
//     var val2 = !n2 ? 0 : n2.val

//     var sum = val1 + val2

//     n1 = n1 ? n1.next : null
//     n2 = n2 ? n2.next : null

//     if (sum >= 10 || node.val + sum == 10) {
//       node.val = (node.val + sum) % 10
//       node.next = new ListNode(1)
//     } else {
//       node.val += sum
//       if (!n1 && !n2) {
//         return start
//       } else {
//         node.next = new ListNode()
//       }
//     }

//     node = node.next
//   }
// }

// var s3 = new ListNode(3)
// var s2 = new ListNode(4, s3)
// var s1 = new ListNode(2, s2)
// var m3 = new ListNode(4)
// var m2 = new ListNode(6, m3)
// var m1 = new ListNode(5, m2)

// console.log(addTwoNumber(s1, m1))

// --------------------------------------------------------------------------

// const parking_exit = (arr) => {
//   let res = []

//   let pos

//   for (i = 0; i < arr.length; i++) {
//     pos = arr[i].indexOf(2) != -1 ? arr[i].indexOf(2) : pos

//     if (arr[i].indexOf(1) != -1 && pos != undefined) {
//       let moves = arr[i].indexOf(1) - pos

//       switch (true) {
//         case moves < 0:
//           res.push('L' + Math.abs(moves))
//           break
//         case moves > 0:
//           res.push('R' + Math.abs(moves))
//           break
//       }

//       pos = arr[i].indexOf(1)

//       count = 1
//       while (arr[Number(i) + 1][pos] == 1) {
//         count += 1
//         i += 1
//       }

//       res.push('D' + count)
//     } else {
//       if (arr[i].length - 1 - pos != 0) {
//         res.push('R' + (arr[i].length - 1 - pos))
//       }
//     }
//   }

//   return res
// }

// console.log(
//   parking_exit([
//     [0, 2, 0, 0, 1],
//     [0, 0, 0, 0, 1],
//     [0, 0, 0, 0, 1],
//     [0, 0, 0, 0, 0],
//   ])
// )

// --------------------------------------------------------------------

// const danceConvert = (pin) => {
//   let res = []

//   const MOVES = [
//     'Shimmy',
//     'Shake',
//     'Pirouette',
//     'Slide',
//     'Box Step',
//     'Headspin',
//     'Dosado',
//     'Pop',
//     'Lock',
//     'Arabesque',
//   ]

//   for (i in pin) {
//     if (isNaN(pin[i])) {
//       return 'Invalid input.'
//     } else {
//       index =
//         Number(pin[i]) + Number(i) < MOVES.length
//           ? Number(pin[i]) + Number(i)
//           : (Number(pin[i]) + Number(i)) % MOVES.length

//       res.push(MOVES[index])
//     }
//   }

//   if (pin.length != 4) {
//     return 'Invalid input.'
//   } else {
//     return res
//   }
// }

// console.log(
//   danceConvert('0000'),
//   danceConvert('3856'),
//   danceConvert('9999'),
//   danceConvert('32a1')
// )

// ----------------------------------------------------------------

// const zeroesToEnd = (nums) => {
//   let z = []

//   while (nums.indexOf(0) != -1) {
//     z.push(...nums.splice(nums.indexOf(0), 1))
//   }
//   nums.push(...z)
//   return nums
// }

// console.log(zeroesToEnd([1, 2, 0, 0, 4, 0, 5]))

// -----------------------------------------------------------------

// const kixCode = (address) => {
//   const houseNum = address.match(/\d+.+(?=,)/)[0].replace(/[^\d\w]/, 'X')
//   const postalCode = address.match(/(?<=, )[\d-]{4}/)[0]
//   const suffix = address.match(/ [A-Z]{2} /)

//   return (postalCode + suffix[0].trim() + houseNum).toUpperCase()
// }

// console.log(
//   kixCode(`PostNL, Postbus 30250, 2500 GG ’s Gravenhage`),
//   kixCode(`Liesanne B Wilkens, Kogge 11-1, 1657 KA Abbekerk`),
//   kixCode('Jet de Wit, Wielingenstraat 129/7, 3522 PG Utrecht')
// )

// ----------------------------------------------------------------

// const recurIndex = (s) => {
//   const hashMap = new Map()

//   for (i in s) {
//     if (hashMap.has(s[i])) {
//       const res = {}
//       res[s[i]] = [Number(hashMap.get(s[i])), Number(i)]
//       return res
//     } else {
//       hashMap.set(s[i], i)
//     }
//   }

//   return {}
// }

// console.log(recurIndex('DXTDXTXDTXD'))

// -------------------------------------------------------------------

// const dominoesFall = (s) => {
//   if (/RI(?!L)|(?<!R)IL/.test(s)) {
//     const regex1 = [...s.matchAll(/RI(?!L)/g)]
//     const regex2 = [...s.matchAll(/(?<!R)IL/g)]

//     let next = s

//     if (regex1.length) {
//       for (i in regex1) {
//         next =
//           next.substr(0, regex1[i].index) +
//           'RR' +
//           next.substr(regex1[i].index + 2)
//       }
//     }
//     if (regex2.length) {
//       for (x in regex2) {
//         next =
//           next.substr(0, regex2[x].index) +
//           'LL' +
//           next.substr(regex2[x].index + 2)
//       }
//     }
//     return dominoesFall(next)
//   } else {
//     return s
//   }
// }

// console.log(dominoesFall('ILIRIIILRIILII'))

// -----------------------------------------------------------

// const maxArea = (height) => {
//   let max = 0
//   for (i = 0; i < height.length; i++) {
//     for (j = i + 1; j < height.length; j++) {
//       const area = (j - i) * Math.min(height[i], height[j])
//       if (area > max) {
//         max = area
//       }
//     }
//   }

//   return max
// }

// console.log(maxArea([2, 3, 4, 5, 18, 17, 6]))

// --------------------------------------------------------

// Slidign window version

// const maxArea = (height) => {
//   var right = height.length - 1
//   var left = 0
//   let res = 0

//   while (left < right) {
//     const area = (right - left) * Math.min(height[right], height[left])
//     if (height[left] < height[right]) {
//       left += 1
//     } else {
//       right -= 1
//     }

//     if (area > res) {
//       res = area
//     }
//   }

//   return res
// }

// console.log(maxArea([2, 3, 4, 5, 18, 17, 6]))

// -----------------------------------------------------------------

// 1,5,15,34,65, 111
// 4, 10, 19,31, 46
// 6, 9,12, 15
// 3, 3, 3

// const rowSum = (n) => {
//   return (n ** 3 + n) / 2
// }

// -------------------------------------------------------------------

// const plusSign = (str) => {
//   const regex = /(?<=\+)[a-zA-Z](?=\+)/g
//   const charCheck = /[a-zA-Z]/g

//   let res = str.replace(regex, '')

//   if (charCheck.test(res)) {
//     return false
//   } else {
//     return true
//   }
// }

// console.log(plusSign('+f+d+c+#+f+'))

// -------------------------------------------------------------------

//Using sliding window
// const isPalindrome = (int) => {
//   if (int < 0) {
//     return false
//   }

//   let num = String(int)
//   let left = 0
//   let right = num.length - 1

//   while (left < right) {
//     if (num[left] == num[right]) {
//       left += 1
//       right -= 1
//     } else {
//       return false
//     }
//   }

//   return true
// }

// console.log(isPalindrome(112321))

// ---------------------------------------------------------------------

// const isPandigital = (num) => {
//   console.log(`${num}`)
//   for (i = 0; i < 10; i++) {
//     console.log(String(num))
//     if (String(num).indexOf(String(i)) == -1) {
//       return false
//     }
//   }

//   return true
// }

// console.log(isPandigital(112233445566778899))

// -----------------------------------------------------------

// const rearrange = (sentence) => {
//   if (sentence.trim() == '') {
//     return ''
//   } else {
//     return sentence
//       .split(' ')
//       .sort((a, b) => {
//         return /\d/.exec(a)[0] - /\d/.exec(b)[0]
//       })
//       .map((word) => {
//         return word.replace(/\d/, '')
//       })
//       .join(' ')
//   }
// }

// rearrange('sf2s rgfsrg1 grd7gdrg fwefe3 gswgdrzfgh7')

// // ------------------------------------------------------------

// const dice = (roll) => {
//   if (roll == 0) {
//     return ''
//   }
//   const rolls = [
//     '---/-O-/---',
//     'O--/---/--O',
//     'O--/-O-/--O',
//     'O-O/---/O-O',
//     'O-O/-O-/O-O',
//     'O-O/O-O/O-O',
//   ]
//   if (roll <= 6) {
//     return rolls[roll - 1]
//   } else {
//     let numDice = Math.floor(roll / 6)
//     let remainder = roll % 6
//     var res = []

//     for (i = 0; i < numDice; i++) {
//       res.unshift(rolls[5])
//     }
//     if (remainder) {
//       res.push(rolls[remainder - 1])
//     }
//     return res.join(', ')
//   }
// }

// dice(20)

// ------------------------------------------------------------

// const ulam = (n) => {
//   var nums = new Map([
//     [1, null],
//     [2, null],
//   ])

//   i = 3
//   while (true) {
//     if (nums.size == n) {
//       return Array.from(nums.keys())[nums.size - 1]
//     }

//     let count = 0

//     for (const item of nums.keys()) {
//       const sumNum = i - item
//       if (nums.has(sumNum) && sumNum != item) {
//         count += 1
//       }
//     }

//     if (count == 2) {
//       nums.set(i, true)
//     }
//     i++
//   }
// }

// console.log(ulam(7))

// ---------------------------------------------------------------

// const switchGravityOn = (state) => {
//   const count = []

//   for (x in state[0]) {
//     count.push(0)
//   }

//   for (i = 0; i < state.length; i++) {
//     for (j = 0; j < state[i].length; j++) {
//       if (state[i][j] == '#') {
//         count[j] += 1
//       }
//     }
//   }

//   let res = []

//   for (k = 0; k < state.length; k++) {
//     let subRes = []
//     for (x = 0; x < count.length; x++) {
//       if (count[x] > 0) {
//         subRes.push('#')
//         count[x] -= 1
//       } else {
//         subRes.push('-')
//       }
//     }

//     res.unshift(subRes)
//   }

//   return res
// }

// console.log(
//   switchGravityOn([
//     ['-', '#', '#', '#', '#', '-'],
//     ['#', '-', '-', '#', '#', '-'],
//     ['-', '#', '-', '-', '-', '-'],
//     ['-', '-', '-', '-', '-', '-'],
//   ])
// )

// --------------------------------------------------------

// const split = (p) => {
//   var left = 0
//   var right = 0
//   var pointer = 0

//   let res = []

//   for (i in p) {
//     if (p[i] == '(') {
//       left += 1
//     }

//     if (p[i] == ')') {
//       right += 1
//     }

//     if (left == right && left + right != 0) {
//       res.push(p.slice(pointer, Number(i) + 1))
//       pointer = Number(i) + 1
//       left = 0
//       right = 0
//     }
//   }

//   return res
// }

// console.log(split('((())())(()(()()))'))

// ------------------------------------------------------------

// const countAndSay = (n) => {
//   res = '1'

//   num = ''
//   countNums = 0

//   while (n > 1) {
//     let numArray = res.match(/(.)\1*/g)

//     let subres = ''

//     for (i in numArray) {
//       subres += String(numArray[i].length) + numArray[i][0]
//     }

//     res = subres
//     n -= 1
//   }

//   return res
// }

// console.log(countAndSay(30))

// --------------------------------------------------------------

// const funcSort = (fns) => {
//   const recursion = (n, count = 0) => {
//     if (typeof n == 'function') {
//       count += 1
//       return recursion(n(), count)
//     }
//     return count
//   }

//   return fns.sort((a, b) => {
//     return recursion(a) - recursion(b)
//   })
// }

// f1 = (_) => 'hello'

// f2 = (_) => (_) => 'edabit'

// f3 = (_) => (_) => (_) => 'user'

// console.log(funcSort([f2, f3, f1]))

// --------------------------------------------------------------

// const dartsSolver = (sections, darts, target) => {
//   let result = []
//   const recursive = (s, d, t, res = []) => {
//     if (t < 0 || d < 0) {
//       return
//     }

//     if (d == 0 && t == 0) {
//       console.log(res)
//       result.push(res.join('-'))
//       return
//     }

//     for (i in s) {
//       recursive(s.slice(i), d - 1, t - s[i], [...res, s[i]])
//     }
//   }

//   recursive(sections, darts, target)

//   return result
// }

// console.log(dartsSolver([3, 7, 11, 14, 18, 20, 25], 3, 32))

// ------------------------------------------------------------------

// const makeChange = (num) => {
//   var q = 0
//   var d = 0
//   var n = 0
//   var p = 0

//   let change = num
//   if (change / 25 >= 1) {
//     q += Math.floor(change / 25)
//     change -= Math.floor(change / 25) * 25
//   }

//   if (change / 10 >= 1) {
//     d += Math.floor(change / 10)
//     change -= Math.floor(change / 10) * 10
//   }

//   if (change / 5 >= 1) {
//     n += Math.floor(change / 5)
//     change -= Math.floor(change / 5) * 5
//   }

//   p = change

//   return { q: q, d: d, n: n, p: p }
// }

// console.log(makeChange(47))

// -------------------------------------------------------------

// const mostExpensive = (obj) => {
//   let res = ''
//   let count = 0

//   for (const item in obj) {
//     if (obj[item] > count) {
//       res = item
//       count = obj[item]
//     }
//   }

//   return `The most expensive one is the ${res}`
// }

// console.log(
//   mostExpensive({
//     'Diamond Earrings': 980,
//     'Gold Watch': 250,
//     'Pearl Necklace': 4650,
//   })
// )

// ----------------------------------------

// const advancedSort = (nums) => {
//   let hashMap = {}

//   for (i in nums) {
//     //JavaScript auto sorts object by key if the key is a number, this is why we put  a ' ' to prevent sorting in this instance.
//     //The alternative is to use the Map() object in order to preserve order of insertion
//     if (hashMap[' ' + String(nums[i])]) {
//       hashMap[' ' + String(nums[i])].push(nums[i])
//     } else {
//       hashMap[' ' + String(nums[i])] = [nums[i]]
//     }
//   }

//   return Object.values(hashMap)
// }

// console.log(advancedSort([6, 2, 1, 2, 2, 1, 3]))

// -----------------------------------------
// Postfix Notation - edabit

// const postfix = (expr) => {
//   const expression = expr.split(' ')

//   if (expression.length == 1) {
//     return Number(expr)
//   }

//   let evalNext = 0
//   let newExpr = []
//   if (isNaN(expression[2])) {
//     eval_next = eval(`${expression[0]} ${expression[2]} ${expression[1]}`)
//     newExpr = expression.slice(3)
//     newExpr.unshift(String(eval_next))
//   } else {
//     eval_next = eval(`${expression[1]} ${expression[3]} ${expression[2]}`)
//     newExpr = expression.slice(4)
//     newExpr.unshift(String(eval_next))
//     newExpr.unshift(expression[0])
//   }

//   return postfix(newExpr.join(' '))
// }

// console.log(postfix('1 1 + 2 2 + -'))

// ------------------------------------------------------

// Lemonade Stand - edabit

// const lemonade = (bills) => {
//   let change = { 5: 0, 10: 0, 20: 0 }

//   for (i in bills) {
//     change[bills[i]] += 1

//     if (bills[i] == 10) {
//       if (change[5] - 1 >= 0) {
//         change[5] -= 1
//       } else {
//         return false
//       }
//     }

//     if (bills[i] == 20) {
//       if (change[10] - 1 >= 0 && change[5] - 1 >= 0) {
//         change[10] -= 1
//         change[5] -= 1
//       } else if (change[5] - 3 >= 0) {
//         change[5] -= 3
//       } else {
//         return false
//       }
//     }
//   }

//   return true
// }

// console.log(
//   lemonade([5, 5, 5, 10, 20]),
//   lemonade([5, 5, 10, 10, 20]),
//   lemonade([10, 10])
// )

// [5, 5, 5, 10, 20, 10]

// ---------------------------------------------------------------

// Splitting Objects Inside a List

// const split_bunches = (bunches) => {
//   let res = []
//   for (i = 0; i < bunches.length; i++) {
//     for (x = 0; x < bunches[i].quantity; x++) {
//       res.push({ name: bunches[i].name, quantity: 1 })
//     }
//   }

//   return res
// }

// console.log(split_bunches([{ name: 'grapes', quantity: 2 }]))

// ---------------------------------------------------------------

// MemeSum - edabit

// const memeSum = (a, b) => {
//   let numA = String(a)
//   let numB = String(b)

//   let res = []

//   for (i = 0; i < Math.max(numA.length, numB.length); i++) {
//     let num1 = numA.length - 1 - i < 0 ? 0 : Number(numA[numA.length - 1 - i])
//     let num2 = numB.length - 1 - i < 0 ? 0 : Number(numB[numB.length - 1 - i])

//     res.unshift(String(num1 + num2))
//   }

//   return Number(res.join(''))
// }

// console.log(memeSum(12439, 26))

// ---------------------------------------------------------------

// First Letter Shift - edabit

// const shiftSentence = (sentence) => {
//   const s = sentence.split(' ')

//   res = []
//   for (i in s) {
//     res.push(s[i - 1 < 0 ? s.length - 1 : i - 1][0] + s[i].slice(1))
//   }

//   return res.join(' ')
// }

// console.log(shiftSentence('create a function'))

// -----------------------------------------------------------------

// Making a Box 2.0 - edabit

// const charBox = (n) => {
//   let res = []

//   if (n == 0) {
//     return [[]]
//   }

//   if (n < 0 || typeof n == 'string' || n % 1 != 0) {
//     return -1
//   }

//   for (i = 0; i < n; i++) {
//     let sub = []
//     for (j = 0; j < n; j++) {
//       if (i == 0 || i == n - 1) {
//         sub.push('#')
//       } else {
//         if (j == 0 || j == n - 1) {
//           sub.push('#')
//         } else {
//           sub.push(' ')
//         }
//       }
//     }
//     res.push(sub)
//   }
//   return res
// }

// console.log(typeof -0.23)

// --------------------------------------------------------------

// Permutations - leetcode

// Backtracking

// const permute = (nums) => {
//   let res = []
//   const backtracking = (n, r = []) => {
//     if (n.length == 0) {
//       res.push(r)
//     }
//     for (let i = 0; i < n.length; i++) {
//       backtracking(n.slice(0, i).concat(n.slice(i + 1)), [...r, n[i]])
//     }
//   }

//   backtracking(nums)

//   return res
// }

// console.log(permute([1, 2, 3]))

// ---------------------------------------------------------------------

// Cup Swapping - edabit

// const cup_swapping = (swaps) => {
//   let pos = { A: false, B: true, C: false }

//   for (i in swaps) {
//     ;[pos[swaps[i][0]], pos[swaps[i][1]]] = [pos[swaps[i][1]], pos[swaps[i][0]]]
//   }

//   for (const h in pos) {
//     if (pos[h]) {
//       return h
//     }
//   }
// }

// console.log(cup_swapping(['AB', 'CA', 'AB']))

// --------------------------------------------------------------

// Clockwise Cipher - edabit

// function clockwiseCipher(message) {
//   message = [...message]
//   const size = Math.ceil(Math.sqrt(message.length))
//   let square = Array.from({ length: size }, (_) => new Array(size).fill(' '))
//   let j = 0
//   let k = 4 * (size - 2 * j - 1) || 1

//   while (k > 0) {
//     console.log(square, message)
//     for (let i = 0; i < k && message.length; i++) {
//       let y, x
//       if (i % 4 === 0) [y, x] = [j, i / 4 + j]
//       if (i % 4 === 1) [y, x] = [(i - 1) / 4 + j, size - 1 - j]
//       if (i % 4 === 2) [y, x] = [size - 1 - j, size - 1 - ((i - 2) / 4 + j)]
//       if (i % 4 === 3) [y, x] = [size - 1 - ((i - 3) / 4 + j), j]
//       square[y][x] = message.shift()
//     }
//     j++
//     k = 4 * (size - 2 * j - 1) || 1
//   }

//   return square.flat().join('')
// }

// console.log(clockwiseCipher('Mubashir Hassan'))

// --------------------------------------------------------

// Complex Number Sum - edabit

// const sumComplex = (numList) => {
//   let regex_i = /[+-][0-9i]+(?=i)/g
//   let regex_n = /[+-]?[0-9]+(?![0-9i]+)/g
//   let regex_additional = /[+-]?(?<![0-9])i/g

//   const nums = numList.join('+')

//   let i =
//     nums.match(regex_i) != null
//       ? Number(
//           nums.match(regex_i).reduce((a, b) => {
//             return Number(a) + Number(b)
//           })
//         )
//       : 0

//   let n =
//     nums.match(regex_n) != null
//       ? Number(
//           nums.match(regex_n).reduce((a, b) => {
//             return Number(a) + Number(b)
//           })
//         )
//       : 0

//   const additionals =
//     nums.match(regex_additional) != null ? nums.match(regex_additional) : []

//   for (h in additionals) {
//     if (additionals[h][0] == '-') {
//       i -= 1
//     } else {
//       i += 1
//     }
//   }

//   let res = ''

//   if (n > 0) {
//     res += n
//   }

//   if (n < 0) {
//     res += n
//   }

//   if (n != 0 && i > 0) {
//     res += '+' + `${i == 1 ? '' : i == -1 ? '-' : i}` + 'i'
//   }

//   if (n != 0 && i < 0) {
//     res += `${i == 1 ? '' : i == -1 ? '-' : i}` + 'i'
//   }

//   if (n == 0 && i != 0) {
//     res += `${i == 1 ? '' : i == -1 ? '-' : i}` + 'i'
//   }

//   if (res == '') {
//     return '0'
//   } else {
//     return res
//   }
// }

// console.log(sumComplex(['123+456i']))

// --------------------------------------------------------------------

// Can You Make the Numbers? - edabit

// const canBuild = (digits, arr) => {
//   let d = digits

//   for (i in arr) {
//     let n = String(arr[i])

//     for (x in n) {
//       if (d[Number(n[x])] > 0) {
//         d[Number(n[x])] -= 1
//       } else {
//         return false
//       }
//     }
//   }

//   return true
// }

// console.log(canBuild([0, 1, 2, 2, 3, 0, 0, 0, 1, 1], [123, 444, 92]))
// console.log(canBuild([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3]))
// console.log(canBuild([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], []))

// ------------------------------------------------------

// Ungroop Datae in an Object - edabit

// const ungroupStudents = (students) => {
//   let res = []

//   for (i in students) {
//     let s = { teacher: students[i].teacher }

//     for (x in students[i].data) {
//       res.push({ teacher: students[i].teacher, ...students[i].data[x] })
//     }
//   }
//   return res
// }

// console.log(
//   ungroupStudents([
//     {
//       teacher: 'Ms. Car',
//       data: [
//         {
//           name: 'James',
//           emergenceNumber: '617-771-1082',
//         },
//         {
//           name: 'Alice',
//           alergies: ['nuts', 'carrots'],
//         },
//       ],
//     },
//     {
//       teacher: 'Mr. Lamb',
//       data: [
//         {
//           name: 'Aaron',
//           age: 3,
//         },
//       ],
//     },
//   ])
// )

// ------------------------------------------------------------------------

// A Watermelon - edabit

// const totalSeeds = (watermelon) => {
//   let res = 0
//   for (i = 0; i < 2; i++) {
//     let h1 = 0
//     let h2 = 0
//     for (
//       x = i * (watermelon.length / 2);
//       x < i * (watermelon.length / 2) + watermelon.length / 2;
//       x++
//     ) {
//       for (s = 0; s < watermelon[x].length; s++) {
//         if (watermelon[x][s] == 1 && watermelon[x].length / s > 2) {
//           h1 += 1
//         }

//         if (watermelon[x][s] == 1 && watermelon[x].length / s <= 2) {
//           h2 += 1
//         }
//       }
//     }

//     if (h1 > 5) {
//       res += h1
//     }

//     if (h2 > 5) {
//       res += h2
//     }
//   }

//   return res
// }

// const w = [
//   [1, 0, 0, 1, 1, 1, 0, 1],
//   [1, 0, 1, 0, 1, 1, 0, 0],
//   [1, 1, 1, 1, 0, 0, 0, 0],
//   [0, 1, 0, 1, 1, 1, 1, 0],
//   [0, 0, 0, 1, 0, 1, 0, 0],
//   [1, 1, 1, 0, 0, 0, 1, 1],
//   [1, 0, 1, 1, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 0, 0, 0],
// ]

// console.log(totalSeeds(w))

// -----------------------------------------------------------------

// Mutations Only - edabit

// const zeroesToEnd = (nums) => {
//   for (let i = nums.length - 1; i >= 0; i--) {
//     if (nums[i] == 0) {
//       nums.push(nums.splice(i, 1)[0])
//     }
//   }

//   return nums
// }

// console.log(zeroesToEnd([1, 2, 0, 0, 4, 0, 5]))

// -----------------------------------------------------------------

// Cleaning Project Files - edabit

// const cleanUp = (files, method) => {
//   const regex = method == 'prefix' ? /.+(?=\.)/g : /(?<=\.).+/g

//   let res = {}

//   for (i in files) {
//     const match = files[i].match(regex)[0]

//     if (match in res) {
//       res[match].push(files[i])
//     } else {
//       res[match] = [files[i]]
//     }
//   }

//   return Object.values(res)
// }

// console.log(cleanUp(['ex1.html', 'ex1.js', 'ex2.html', 'ex2.js'], 'prefix'))

// ----------------------------------------------------------------

// Searching Two Objects at Once - edabit

// // english class object
// const english = {
//   advanced: {
//     // advanced curriculum
//     teacher: 'Ms. Abrimian',
//     acceptsLateWork: false,
//   },
//   standard: {
//     // standard curriculum
//     teacher: 'Mr. Sheehan',
//     acceptsLateWork: true,
//   },
// }

// // math class object
// const math = {
//   advanced: {
//     teacher: 'Mr. Citrano',
//     acceptsLateWork: false,
//   },
//   standard: {
//     teacher: 'Ms. Marinelli',
//     acceptsLateWork: false,
//   },
// }

// const acceptsLateWork = (teacher) => {
//   const teachers = Object.values(english).concat(Object.values(math))

//   return teachers.filter((t) => {
//     return teacher == t.teacher
//   })[0].acceptsLateWork
// }

// console.log(acceptsLateWork('Mr. Citrano'))

// -----------------------------------------------------------------------------

// Remove Computer Virus - edabit

// const removeVirus = (files) => {
//   const regex = /(?<!anti|not)virus|malware/

//   let f = files.split(', ').filter((file) => {
//     return !regex.test(file)
//   })

//   if (f.length == 0) {
//     return 'PC Files: Empty'
//   } else {
//     return f.join(', ')
//   }
// }

// console.log(removeVirus('PC Files: virus.exe, bestmalware.exe, memzvirus.exe'))

// -----------------------------------------------------------------------------

// Wheres the Bomb? - edabit

// const bomb = (p) => {
//   const sound = 0.343

//   const distance = (pos1, pos2) => {
//     return Math.sqrt(
//       Math.pow(pos2[0] - pos1[0], 2) + Math.pow(pos2[1] - pos1[1], 2)
//     ).toFixed(1)
//   }

//   for (i = 0; i < 51; i++) {
//     for (j = 0; j < 51; j++) {
//       if (
//         distance(p[0], [i, j]) == (sound * p[0][2]).toFixed(1) &&
//         distance(p[1], [i, j]) == (sound * p[1][2]).toFixed(1) &&
//         distance(p[2], [i, j]) == (sound * p[2][2]).toFixed(1)
//       ) {
//         return [i, j]
//       }
//     }
//   }
// }

// console.log(
//   bomb([
//     [3, 49, 127.815],
//     [16, 27, 58.672],
//     [11, 40, 92.792],
//   ])
// )

// ----------------------------------------------------------------------

// Books and Book Ends - edabit

// const countUniqueBooks = (stringSequence, bookend) => {
//   let b = false
//   let count = 0
//   let books = []

//   for (i in stringSequence) {
//     if (
//       b === true &&
//       stringSequence[i] != bookend &&
//       books.indexOf(stringSequence[i]) == -1
//     ) {
//       books.push(stringSequence[i])
//       count += 1
//     }

//     if (stringSequence[i] == bookend) {
//       b = b ? false : true
//     }
//   }

//   return count
// }

// console.log(countUniqueBooks('AZYWABBCATTTA', 'A'))

// -----------------------------------------------------------

// Inside, not Outside a Box - edabit

// const count = (box) => {
//   const regex = /(?<=#)[^#]+(?=#)/g

//   let items = []

//   for (i in box) {
//     let item = box[i].match(regex)

//     if (item != null) {
//       for (x in item[0]) {
//         if (item[0][x] != ' ' && !(item[0][x] in items)) {
//           items.push(item[0][x])
//         }
//       }
//     }
//   }

//   return new Set(items).size
// }

// console.log(
//   count(['??????Z', 'Z?####?V', '$?#  #?X', '$@#BA#?P', '$T####?T', 'ZAAAAAAT'])
// )

// ---------------------------------------------------------

// Calculate Depth of Array - edabit

// const depth = (arr) => {
//   let count = 0
//   const r = (n, c = 0) => {
//     if (Array.isArray(n)) {
//       for (i in n) {
//         r(n[i], c + 1)
//       }
//     }
//     if (c > count) {
//       count = c
//     }
//   }

//   r(arr)

//   return count
// }

// console.log(typeof [1, 2])

// console.log(depth([1, [2], 3, [4], 5, [6]]))

// ----------------------------------------------------------------

// Simplify Path - leetcode

// const simplifyPath = (path) => {
//   const p = path.split('/')

//   let res = []

//   for (i in p) {
//     if (p[i].length > 0) {
//       switch (true) {
//         case p[i] == '.':
//           continue
//         case p[i] == '..':
//           if (res.length > 0) {
//             res.pop()
//           }
//           break
//         default:
//           res.push(p[i])
//       }
//     }
//   }

//   return '/' + res.join('/')
// }

// console.log(simplifyPath('/a/./b/../../c/'))

// -----------------------------------------------------

// Level Order Traversal - edabit

// class Node {
//   constructor(data) {
//     this.data = data
//     this.right = null
//     this.left = null
//   }
// }

// class BST {
//   constructor() {
//     this.root = null
//   }
//   insert(element) {
//     const node = new Node(element)
//     if (!this.root) {
//       this.root = node
//     } else {
//       this.insertNode(this.root, node)
//     }
//   }
//   insertNode(node, newNode) {
//     if (node.data > newNode.data) {
//       if (!node.left) {
//         node.left = newNode
//       } else {
//         this.insertNode(node.left, newNode)
//       }
//     } else {
//       if (!node.right) {
//         node.right = newNode
//       } else {
//         this.insertNode(node.right, newNode)
//       }
//     }
//   }
//   // Write your code here
//   traverse() {
//     let res = []

//     let nodes = [this.root]

//     while (true) {
//       let c = []

//       for (let i = 0; i < nodes.length; i++) {
//         res.push(nodes[i].data)

//         if (nodes[i].left != null) {
//           c.push(nodes[i].left)
//         }

//         if (nodes[i].right != null) {
//           c.push(nodes[i].right)
//         }
//       }

//       if (c.length == 0) {
//         break
//       }

//       nodes = c
//     }

//     return res
//   }
//   // End
// }

// const b = new BST()
// b.insert(100)
// b.insert(200)
// b.insert(70)
// b.insert(34)
// b.insert(80)
// b.insert(85)
// b.insert(85)
// b.insert(111)

// console.log(b.traverse())

// ----------------------------------------------------------------------

// Coffee Shop - edabit

// class CoffeeShop {
//   constructor(name, menu, orders) {
//     this.name = name
//     this.menu = menu
//     this.orders = orders
//   }

//   addOrder(order) {
//     let menuItem = this.menu.filter((x) => {
//       return x.item == order
//     })

//     if (menuItem.length > 0) {
//       this.orders.push(menuItem[0])
//       return 'Order added!'
//     } else {
//       return 'This item is currently unavailable!'
//     }
//   }

//   fulfillOrder() {
//     if (this.orders.length > 0) {
//       return `The ${this.orders.shift().item} is ready!`
//     } else {
//       return 'All orders have been fulfilled!'
//     }
//   }

//   listOrders() {
//     return this.orders.map((i) => {
//       return i.item
//     })
//   }

//   dueAmount() {
//     return +this.orders
//       .reduce((a, b) => {
//         return a + b.price
//       }, 0)
//       .toFixed(2)
//   }

//   cheapestItem() {
//     return [...this.menu].sort((a, b) => {
//       return a.price - b.price
//     })[0].item
//   }

//   drinksOnly() {
//     return this.menu
//       .filter((i) => {
//         return i.type == 'drink'
//       })
//       .map((x) => {
//         if (x.type == 'drink') {
//           return x.item
//         }
//       })
//   }

//   foodOnly() {
//     return this.menu
//       .filter((i) => {
//         return i.type == 'food'
//       })
//       .map((x) => {
//         if (x.type == 'food') {
//           return x.item
//         }
//       })
//   }
// }
// let [menuA, menuB, menuC] = [
//     [
//       ['orange juice', 'drink', 2.13],
//       ['lemonade', 'drink', 0.85],
//       ['cranberry juice', 'drink', 3.36],
//       ['pineapple juice', 'drink', 1.89],
//       ['lemon iced tea', 'drink', 1.28],
//       ['apple iced tea', 'drink', 1.28],
//       ['vanilla chai latte', 'drink', 2.48],
//       ['hot chocolate', 'drink', 0.99],
//       ['iced coffee', 'drink', 1.12],
//       ['tuna sandwich', 'food', 0.95],
//       ['ham and cheese sandwich', 'food', 1.35],
//       ['bacon and egg', 'food', 1.15],
//       ['steak', 'food', 3.28],
//       ['hamburger', 'food', 1.05],
//       ['cinnamon roll', 'food', 1.05],
//     ],
//     [
//       ['turkey english muffin', 'food', 7.99],
//       ['avocado toast', 'food', 5.05],
//       ['chocolate croissant', 'food', 3.0],
//       ['espresso', 'drink', 2.99],
//       ['iced caramel macchiato', 'drink', 4.5],
//       ['cortado', 'drink', 4.0],
//       ['nitro cold brew tester', 'drink', 8.0],
//     ],
//     [
//       ['cheeseburger with fries', 'food', 5.44],
//       ['cinnamon roll', 'food', 4.99],
//       ['hot chocolate', 'drink', 2.99],
//       ['lemon tea', 'drink', 2.5],
//       ['iced coffee', 'drink', 3.0],
//       ['vanilla chai latte', 'drink', 4.0],
//     ],
//   ].reduce(
//     (a, r) => [
//       ...a,
//       [...r.map(([n, t, p]) => ({ item: n, type: t, price: p }))],
//     ],
//     []
//   ),
//   [shopA, shopB, shopC] = [
//     new CoffeeShop('*** Deep Into Coffee ***', menuA, []),
//     new CoffeeShop("*** Xavier's ***", menuB, []),
//     new CoffeeShop("*** Tesha's ***", menuC, []),
//   ]

// console.log(shopC.drinksOnly())

// ------------------------------------------------------------------

// Shared vs Unique Letters - edabit

// const letters = (w1, w2) => {
//   const chars = new Set((w1 + w2).split('').sort())

//   let res = ['', '', '']

//   chars.forEach((char) => {
//     switch (true) {
//       case w1.indexOf(char) != -1 && w2.indexOf(char) != -1:
//         res[0] += char
//         break
//       case w1.indexOf(char) != -1:
//         res[1] += char
//         break
//       case w2.indexOf(char) != -1:
//         res[2] += char
//         break
//     }
//   })

//   return res
// }

// console.log(letters('sharp', 'soap'))

// -----------------------------------------------------

// Excel Sheet Column Number - edabit

// const title_to_number = (s) => {
//   const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

//   let count = 0

//   for (i in s) {
//     let pos = alphabet.indexOf(s[i]) + 1

//     let m1 = s.length - (+i + 1)

//     count += pos * alphabet.length ** m1
//   }

//   return count
// }

// console.log(title_to_number('FANG'))

// ------------------------------------------------------

// Grocery Store Prices - edabit

// const getPrices = (s) => {
//   return s
//     .join(' ')
//     .match(/(?<=\(\$).+?(?=\))/g)
//     .map((price) => {
//       return parseFloat(price)
//     })
// }

// console.log(
//   getPrices([
//     'ice cream ($5.99)',
//     'banana ($0.20)',
//     'sandwich ($8.50)',
//     'soup ($1.99)',
//   ])
// )

// ---------------------------------------------------

// Find All Digits - edabit

// const findAllDigits = (nums) => {
//   let digits = '0123456789'

//   for (let i of nums) {
//     String(i)
//       .split('')
//       .forEach((num) => {
//         digits = digits.replace(num, '')
//       })

//     if (digits.length < 1) {
//       return i
//     }
//   }

//   return 'Missing digits!'
// }

// console.log(
//   findAllDigits([5175, 4538, 2926, 5057, 6401, 4376, 2280, 6137, 8798, 9083])
// )

// --------------------------------------------------------

// Dice Score - edabit

// const diceScore = (dice) => {
//   let hashMap = {}

//   for (i in dice) {
//     if (String(dice[i]) in hashMap) {
//       hashMap[String(dice[i])] += 1
//     } else {
//       hashMap[String(dice[i])] = 1
//     }
//   }

//   let count = 0

//   for (i in hashMap) {
//     switch (true) {
//       case i == '1':
//         count += Math.floor(hashMap[i] / 3) * 1000
//         count += (hashMap[i] % 3) * 100
//         break
//       case i == '2':
//         count += Math.floor(hashMap[i] / 3) * 200
//         break
//       case i == '3':
//         count += Math.floor(hashMap[i] / 3) * 300
//         break
//       case i == '4':
//         count += Math.floor(hashMap[i] / 3) * 400
//         break
//       case i == '5':
//         count += Math.floor(hashMap[i] / 3) * 500
//         count += (hashMap[i] % 3) * 50
//         break
//       case i == '6':
//         count += Math.floor(hashMap[i] / 3) * 600
//         break
//     }
//   }

//   return count
// }

// console.log(diceScore([4, 4, 4, 3, 3]))

// ----------------------------------------------------------------------

// The Susquehanna Hat Company - edabit

// const hats = (arr) => {
//   const target = arr[0]

//   const production = arr[1]

//   let count = 0
//   let i = 1

//   while (true) {
//     if (count > target) {
//       return 'None'
//     }

//     for (x in production) {
//       if (i % production[x] == 0) {
//         count += 1
//       }
//     }

//     if (count == target) {
//       return `${i} minutes`
//     }
//     i++
//   }
// }

// -------------------------------------------------------------------

// an OSHA Approved Ladder - edabit

// const isLadderSafe = (ladder) => {
//   let rungs = []
//   let width = ladder[0].length

//   if (width < 5) {
//     return false
//   }

//   for (i in ladder) {
//     // Check width
//     if (ladder[i].length < 5 || ladder[i].length != width) {
//       return false
//     }

//     //Check for broken rungs
//     let s = ladder[i].slice(1, ladder[i].length - 1).split('')
//     if (
//       !s.every((char) => {
//         return char == s[0]
//       })
//     ) {
//       return false
//     }

//     // Check rungs
//     if (ladder[i].indexOf(' ') == -1) {
//       rungs.push(i)
//     }
//   }

//   let count = Number(rungs[1]) - Number(rungs[0])

//   for (x in rungs) {
//     if (x != 0) {
//       if (rungs[x] - rungs[+x - 1] != count || rungs[x] - rungs[+x - 1] > 3) {
//         return false
//       }
//     }
//   }

//   if (rungs.length < 1) {
//     return false
//   }

//   return true
// }

// console.log(
//   isLadderSafe([
//     '#   #',
//     '#####',
//     '#   #',
//     '#   #',
//     '#####',
//     '#   #',
//     '#   #',
//     '#####',
//     '#   #',
//   ])
// )

// -------------------------------------------------------------

// Remove Duplicates from Sorted Array

// const removeDuplicates = (nums) => {
//   if (nums.length == 0) {
//     return 0
//   }

//   let i = 1

//   while (true) {
//     if (nums[i] == '-' || i >= nums.length) {
//       return i
//     }

//     if (nums[i] == nums[i - 1]) {
//       nums.splice(i, 1)
//       nums.push('-')
//     } else {
//       i++
//     }
//   }
// }

// console.log(removeDuplicates([1, 1]))

// -------------------------------------------------------

// Build a Diamond Machine - edabit

// const diamond = (n) => {
//   let left = n % 2 == 0 ? n / 2 - 1 : Math.floor(n / 2)
//   let right = n % 2 == 0 ? n / 2 : Math.floor(n / 2)

//   let d = []

//   while (left > 0 && right < n - 1) {
//     let diamondCut = []
//     for (let i = 0; i < n; i++) {
//       if (i == left || i == right) {
//         diamondCut.push(1)
//       } else {
//         diamondCut.push(0)
//       }
//     }
//     d.push(diamondCut)
//     left -= 1
//     right += 1
//   }

//   while (left <= right) {
//     let diamondCut = []
//     for (let i = 0; i < n; i++) {
//       if (i == left || i == right) {
//         diamondCut.push(1)
//       } else {
//         diamondCut.push(0)
//       }
//     }
//     d.push(diamondCut)
//     left += 1
//     right -= 1
//   }

//   return [d, n % 2 == 0 ? 'good cut' : 'perfect cut']
// }

// console.log(diamond(10))

// --------------------------------------------------------

// Burglary Series (12): Get Vodka Bottle - edabit

// const getVodkaBottle = (obj, num) => {
//   for (let i in obj) {
//     if (obj[i] == num && i.indexOf('Rammstein') != -1) {
//       return i
//     }
//   }
// }

// console.log(
//   getVodkaBottle({ whiskey: 100, 'Rammstein A': 100, 'Rammstein B': 50 }, 100)
// )

// --------------------------------------------------------

// Simple Counting - edabit

// const countDigits = (n, d) => {
//   let count = 0
//   const r = new RegExp(`${d}`, 'g')
//   for (let i = 0; i <= n; i++) {
//     count +=
//       String(Math.pow(i, 2)).match(r) != null &&
//       String(Math.pow(i, 2)).match(r).length
//   }

//   return count
// }

// console.log(countDigits(10, 1))

// ---------------------------------------------------------

// Multiplication tables - edabit

// const mulTable = (n) => {
//   let res = []
//   for (i = 1; i <= n; i++) {
//     let sub = []
//     for (x = 1; x <= n; x++) {
//       sub.push(i * x)
//     }

//     res.push(sub)
//   }

//   return res
// }

// console.log(mulTable(5))

// --------------------------------------------------------

// Mowing the lawn - edabit

// const cuttingGrass = (grass, ...args) => {
//   let res = []
//   for (i in args) {
//     let done = false
//     for (x in grass) {
//       if (grass[x] - args[i] <= 0) {
//         done = true
//       }
//       grass[x] -= args[i]
//     }
//     if (done) {
//       res.push('Done')
//     } else {
//       res.push([...grass])
//     }
//   }
//   return res
// }

// console.log(cuttingGrass([4, 2, 2], 2, 1, 1))

// -------------------------------------------------------

// Enter the Matrix - edabit

// const transposeMatrix = (mtx) => {
//   let res = []
//   for (i in mtx[0]) {
//     for (x in mtx) {
//       res.push(mtx[x][i])
//     }
//   }

//   return res.join(' ')
// }

// console.log(transposeMatrix([['Enter'], ['the'], ['Matrix!']]))

// ----------------------------------------------------

// Name Count Equality - edabit

// const equalCount = (str, names) => {
//   let n = names.split('&')

//   let res = {}

//   for (i in n) {
//     const r = new RegExp(n[i], 'g')
//     let matches = str.match(r)
//     res[n[i]] = matches != null ? matches.length : 0
//   }

//   if (Object.values(res)[0] == Object.values(res)[1]) {
//     res.equality = true
//   } else {
//     res.equality = false
//     res.difference = Math.abs(Object.values(res)[1] - Object.values(res)[0])
//   }

//   return res
// }

// console.log(
//   equalCount(
//     'Elliot!@#$Sam!--@|#$Elliot@|Sam++Elliot$%^Elliot@|Sam!@#Elliot!@#$Sam!--@|#$Elliot',
//     'Sam&Elliot'
//   )
// )

// -------------------------------------------------------------------

// Column with Maximum Sum - edabit

// const colWithMaxSum = (nums, n) => {
//   let res = Array.from(Array(n), () => {
//     return []
//   })
//   let i = 0

//   while (i < nums.length) {
//     res[i % n].push(nums[i])
//     i++
//   }

//   let sums = res.map((item) =>
//     item.reduce((a, b) => {
//       return a + b
//     })
//   )

//   console.log(res, sums)
//   return sums.indexOf(Math.max(...sums)) + 1
// }

// console.log(colWithMaxSum([4, 14, 12, 7, 14, 16, 5, 13, 7, 16, 11, 19], 4))

// -------------------------------------------------------------------

// Message from Space - edabit

// const space_message = (str) => {
//   let regex = /\[[^\[\]]+\]/

//   if (!regex.test(str)) {
//     return str
//   }

//   let main = str.match(regex)[0]
//   let chars = main.match(/[A-Z]+/g)[0].repeat(+main.match(/\d+/g)[0])
//   let newString = str.replace(regex, chars)

//   return space_message(newString)
// }

// console.log(space_message('AB[2C[2EF]G]'))

// -----------------------------------------------------------------

// Coin Trouble - edabit

// const sum = (arr) => arr.reduce((acc, v) => acc + v, 0)

// const coinsDiv = (arr) => {
//   const coins = arr.sort((a, b) => a - b)
//   const total = sum(coins)
//   const third = total / 3

//   const parts = Array(3).fill(third)

//   for (let i = 0; i < 3; i++)
//     while (parts[i]) {
//       console.log(parts)
//       let idx = coins.findIndex((coin) => coin === parts[i])
//       if (idx === -1) idx = coins.findIndex((coin) => coin < parts[i])
//       if (idx === -1) return false
//       else parts[i] -= coins.splice(idx, 1)
//     }

//   return true
// }

// coinsDiv([2, 4, 3, 2, 4, 9, 7, 8, 6, 9])

// ----------------------------------------------------------------

// // MTG Mana Costs - edabit

// const can_pay_cost = (mana, cost) => {
//   let mana_pool = mana

//   const chars = /[A-Z]+/g.test(cost) ? cost.match(/[A-Z]+/g)[0] : ''
//   const nums = /[0-9]+/g.test(cost) ? +cost.match(/[0-9]+/g) : 0

//   for (i in chars) {
//     if (mana_pool.indexOf(chars[i]) == -1) {
//       return false
//     } else {
//       mana_pool = mana_pool.replace(chars[i], '')
//     }
//   }
//   if (mana_pool.length < nums) {
//     return false
//   }

//   return true
// }

// console.log(can_pay_cost('WWWWUUUUBBBBRR', '13RR'))

// ---------------------------------------------------------------

// I Made a Mistake - edabit

// const getValue = (arrs) => {
//   if (!Array.isArray(arrs[0])) {
//     if (arrs[0]) {
//       return arrs[0]
//     } else {
//       return 'What... why did you make this?'
//     }
//   }

//   return getValue(arrs.flat())
// }

// console.log(getValue([[[[[[[[[[[]]]]]]]]]]]))
// console.log(getValue([[[[[[[[[[[[[[[['Bazinga']]]]]]]]], []]]]]]]]))

// ---------------------------------------------------------------

// Longest Slide - edabit

// const longestSlide = (pyramid) => {
//   let count = 0

//   const recursion = (level, pos, sum) => {
//     if (level >= pyramid.length && sum > count) {
//       count = sum
//       return
//     }

//     if (level < pyramid.length) {
//       let right = pos + 1
//       let left = pos

//       recursion(level + 1, left, sum + pyramid[level][pos])
//       recursion(level + 1, right, sum + pyramid[level][pos])
//     }
//   }

//   recursion(0, 0, 0)

//   return count
// }

// console.log(longestSlide([[2], [9, 4], [1, 8, 7], [6, 4, 7, 2]]))

// ----------------------------------------------------------

// More efficient pyramid solution

// Longest Slide - edabit

// const longestSlide = (pyramid) => {
//   for (let i = pyramid.length - 2; i >= 0; i--) {
//     for (let j = 0; j < pyramid[i].length; j++) {
//       pyramid[i][j] =
//         pyramid[i][j] + Math.max(pyramid[i + 1][j], pyramid[i + 1][j + 1])
//     }
//   }

//   return pyramid[0][0]
// }

// console.log(longestSlide([[2], [9, 4], [1, 8, 7], [6, 4, 7, 2]]))

// ----------------------------------------------------------

// East or West - edabit

// const direciton = (arr) => {
//   let res = []

//   for (i in arr) {
//     let n1 = arr[i]
//       .replace('e', 'w')
//       .replace('E', 'W')
//       .replace('a', 'e')
//       .replace('A', 'E')

//     res.push(n1)
//   }

//   return res
// }

// console.log(direciton(['east EAST', 'e a s t', 'E A S T']))

// -------------------------------------------------------------

// Seven Boom - edabit

// const sevenBoom = (nums) => {
//   for (i in nums) {
//     if (String(nums[i]).indexOf('7') != -1) {
//       return 'Boom!'
//     }
//   }

//   return 'there is no 7 in the array'
// }

// console.log(sevenBoom([1, 2, 3, 4, 5, 6, 0]))

// ----------------------------------------------------------------

// The GPS itinerary: Around the World - edabit

// Utility Class
// With utility functions you can call the method straight from the class (e.g. GPS.decimal()) without having to instantiate the object

// Haversine Formular
// a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
// c = 2 ⋅ atan2( √a, √(1−a) )
// d = R ⋅ c

// Note:
// φ = latitude (radians)
// λ = longittude (radians)

// class GPS {
//   static decimal(degrees, minutes, seconds, directions) {
//     return directions == 'S' || directions == 'W'
//       ? (degrees + minutes / 60 + seconds / 3600) * -1
//       : degrees + minutes / 60 + seconds / 3600
//   }

//   static radians(decimal) {
//     return (decimal * Math.PI) / 180
//   }

//   static distance(cityA, cityB) {
//     //City latitude and longitude (Coordinates --> Decimals --> Radians)

//     const cityA_lat = this.radians(
//       this.decimal(
//         ...cityA
//           .replace(/[^A-Za-z0-9 ]/g, '')
//           .split(' ')
//           .slice(0, 4)
//           .map((char) => {
//             if (!isNaN(char)) {
//               return Number(char)
//             } else {
//               return char
//             }
//           })
//       )
//     )

//     const cityA_lon = this.radians(
//       this.decimal(
//         ...cityA
//           .replace(/[^A-Za-z0-9 ]/g, '')
//           .split(' ')
//           .slice(4)
//           .map((char) => {
//             if (!isNaN(char)) {
//               return Number(char)
//             } else {
//               return char
//             }
//           })
//       )
//     )

//     const cityB_lat = this.radians(
//       this.decimal(
//         ...cityB
//           .replace(/[^A-Za-z0-9 ]/g, '')
//           .split(' ')
//           .slice(0, 4)
//           .map((char) => {
//             if (!isNaN(char)) {
//               return Number(char)
//             } else {
//               return char
//             }
//           })
//       )
//     )
//     const cityB_lon = this.radians(
//       this.decimal(
//         ...cityB
//           .replace(/[^A-Za-z0-9 ]/g, '')
//           .split(' ')
//           .slice(4)
//           .map((char) => {
//             if (!isNaN(char)) {
//               return Number(char)
//             } else {
//               return char
//             }
//           })
//       )
//     )

//     const R = 6371e3 // Raidus of Earth (metres)
//     const diff_lat = cityB_lat - cityA_lat
//     const diff_lon = cityB_lon - cityA_lon

//     const a =
//       Math.pow(Math.sin(diff_lat / 2), 2) +
//       Math.cos(cityB_lat) *
//         Math.cos(cityA_lat) *
//         Math.pow(Math.sin(diff_lon / 2), 2)

//     const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))

//     return Math.floor((R * c) / 1000) // kilometers
//   }
// }

// // Itinerary Function

// const itinerary = (start, toVisit) => {
//   let unvisited = [...toVisit]
//   let visited = [start]

//   let count = 0

//   let current = start

//   while (visited.length <= toVisit.length) {
//     let distancesFromCurrent = unvisited.map((city) => {
//       return GPS.distance(cities[current], cities[city])
//     })

//     let min_index = distancesFromCurrent.indexOf(
//       Math.min(...distancesFromCurrent)
//     )

//     count += Math.min(...distancesFromCurrent)

//     current = unvisited[min_index]

//     visited.push(...unvisited.splice(min_index, 1))
//   }

//   return [visited, count]
// }

// const cities = {
//   London: `51° 30' 30" N 0° 7' 32" W`,
//   'New York': `40° 42' 51" N 74° 0' 21" W`,
//   Kitchener: `43° 27' 10" N 80° 29' 42" W`,
//   'Los Angeles': `34° 3' 8" N 118° 14' 37" W`,
//   Naples: `40° 51' 46" N 14° 16' 36" E`,
//   Moscow: `55° 45' 7" N 37° 36' 56" E`,
//   Beijing: `39° 54' 27" N 116° 23' 50" E`,
//   Tokyo: `35° 41' 22" N 139° 41' 30" E`,
//   Quito: `0° 13' 47" S 78° 31' 29" W`,
//   'Buenos Aires': `34° 36' 30" S 58° 22' 19" W`,
//   'Rio de Janeiro': `22° 54' 10" S 43° 12' 27" W`,
//   Montevideo: `35° 54' 11" S 56° 11' 17" W`,
//   Johannesburg: `26° 12' 8" S 28° 2' 37" E`,
//   Jakarta: `6° 12' 52" S 106° 50' 42" E`,
//   Sidney: `33° 52' 4" S 151° 12' 26" E`,
//   Auckland: `36° 52' 0" S 174° 46' 0" E`,
// }

// console.log(
//   itinerary('Naples', ['New York', 'Johannesburg', 'Beijing', 'Quito'])
// )

// ---------------------------------------------------------------

// // Find Value in a Binary Tree - edabit

// const valueInTree = (tree, val) => {
//   if (tree != null) {
//     if (tree[0] == val) {
//       return true
//     }
//     if (valueInTree(tree[1], val) || valueInTree(tree[2], val)) {
//       return true
//     }
//   }

//   return false
// }

// lst1 = [3, [7, [1, null, null], [8, null, null]], [5, null, [4, null, null]]]
// lst2_8 = [2, null, null]
// lst2_6 = [24, null, null]
// lst2_7 = [18, null, null]
// lst2_4 = [4, lst2_8, null]
// lst2_3 = [12, null, lst2_4]
// lst2_2 = [10, null, lst2_3]
// lst2_1 = [15, lst2_2, null]
// lst2_5 = [6, lst2_6, lst2_7]
// lst2 = [9, lst2_1, lst2_5]
// lst3_1 = [4, null, null]
// lst3_2 = [9, null, null]
// lst3_3 = [21, null, null]
// lst3_4 = [17, null, null]
// lst3_5 = [25, null, null]
// lst3_6 = [18, lst3_5, null]
// lst3_7 = [20, lst3_3, lst3_4]
// lst3_8 = [91, lst3_2, null]
// lst3_9 = [75, null, lst3_1]
// lst3_10 = [45, null, null]
// lst3_11 = [71, null, null]
// lst3_12 = [34, null, null]
// lst3_13 = [11, null, null]
// lst3_14 = [10, lst3_6, lst3_13]
// lst3_15 = [3, lst3_7, lst3_12]
// lst3_16 = [26, lst3_8, lst3_11]
// lst3_17 = [1, lst3_9, lst3_10]
// lst3_18 = [66, lst3_14, lst3_17]
// lst3_19 = [52, lst3_16, lst3_15]
// lst3 = [97, lst3_18, lst3_19]

// console.log(valueInTree(lst1, 7))

// ----------------------------------------------------

// Character Recognition ⁠— What's the Time? edabit

// const whatsTheTime = (bitmap) => {
//   const bitToNum = {
//     111101101101111: 0,
//     '010110010010111': 1,
//     111001111100111: 2,
//     111001111001111: 3,
//     101101111001001: 4,
//     111100111001111: 5,
//     100100111101111: 6,
//     111001001001001: 7,
//     111101111101111: 8,
//     111101111001001: 9,
//   }

//   let nums = [...Array(4)].map((x) => {
//     return []
//   })

//   for (let j = 0; j < 5; j++) {
//     let bitLine = bitmap.slice(j * 17, j * 17 + 17)
//     nums[0] += bitLine.slice(0, 3)
//     nums[1] += bitLine.slice(4, 7)
//     nums[2] += bitLine.slice(10, 13)
//     nums[3] += bitLine.slice(14)
//   }

//   console.log(nums)
//   let time = ''

//   for (i in nums) {
//     console.log(nums[i])
//     time += String(bitToNum[nums[i]])

//     if (i == 1) {
//       time += ':'
//     }
//   }

//   return time
// }

// console.log(
//   whatsTheTime(
//     '1110010000111011110101100100010100101001000011101111010010010001000111101110001110111'
//   )
// )

// ---------------------------------------------------------------

// Bitmap Image Conversion - edabit

// const toBitString = (time) => {
//   const bitToNum = {
//     0: '111101101101111',
//     1: '010110010010111',
//     2: '111001111100111',
//     3: '111001111001111',
//     4: '101101111001001',
//     5: '111100111001111',
//     6: '100100111101111',
//     7: '111001001001001',
//     8: '111101111101111',
//     9: '111101111001001',
//     ':': '000010000010000',
//   }
//   let rows = [...Array(5)].map((x) => {
//     return []
//   })

//   for (let i = 0; i < 5; i++) {
//     for (let j = 0; j < time.length; j++) {
//       rows[i] += String(bitToNum[time[j]].slice(i * 3, i * 3 + 3))
//       if (j == 0 || j == 3) {
//         rows[i] += String(0)
//       }
//     }
//   }

//   return rows.join('')
// }

// console.log(toBitString('05:44'))

// ------------------------------------------------------------------

// Decompose Address - edabit

// const decomposeAddress = (address) => {
//   const regex =
//     /([0-9]+) ([A-Za-z]+ [A-Za-z]{2}) ([A-Za-z ]+), ([A-Z]{2}) ([0-9]+)/g

//   const res = address.matchAll(regex)

//   return [...res][0].slice(1, 6)
// }
// console.log(decomposeAddress('8919 Scarecrow Ct Idaho Falls, ID 80193'))

// -------------------------------------------------------------

// Jump Game - leetcode

// const canJump = (nums) => {
//   if (nums.length == 1) {
//     return true
//   }

//   let count = 1

//   for (let i = nums.length - 2; i >= 0; i--) {
//     if (nums[i] >= count) {
//       count = 0
//     }

//     if (i != 0) {
//       count += 1
//     }
//   }

//   if (count == 0) {
//     return true
//   } else {
//     return false
//   }
// }

// console.log(canJump([2, 3, 1, 1, 4]))

// --------------------------------------------------------------------

// Frequency Distribution - edabit

// const getFrequencies = (arr) => {
//   let frequencies = {}

//   for (i in arr) {
//     if (String(arr[i]) in frequencies) {
//       frequencies[String(arr[i])] += 1
//     } else {
//       frequencies[String(arr[i])] = 1
//     }
//   }

//   return frequencies
// }

// console.log(
//   getFrequencies(['A', 'B', 'A', 'A', 'A']),
//   getFrequencies([true, false, true, false, false])
// )

// -------------------------------------------------------------------

// 111. Minimum Depth of Binary Tree - leetcode

// const minDepth = (root) => {
//   if (root === null) {
//     return 0
//   }

//   let node_levels = [root]

//   let level = 1

//   while (true) {
//     let sub = []
//     for (let i = 0; i < node_levels.length; i++) {
//       if (node_levels[i].left != null) {
//         sub.push(node_levels[i].left)
//       }

//       if (node_levels[i].right != null) {
//         sub.push(node_levels[i].right)
//       }

//       if (node_levels[i].left === null && node_levels[i].right === null) {
//         return level
//       }
//     }

//     node_levels = sub
//     sub = []
//     level += 1
//   }
// }

// ------------------------------------------------------------------

// Nearest Chapter - edabit

// const nearestChapter = (chapt, page) => {
//   const keys = Object.keys(chapt)
//   const vals = Object.values(chapt)

//   let l = []
//   let count = Math.abs(vals[0] - page)

//   for (i in vals) {
//     if (Math.abs(vals[i] - page) <= count) {
//       count = Math.abs(vals[i] - page)
//       l.unshift(keys[i])
//     }
//   }

//   return l[0]
// }

// console.log(
//   nearestChapter(
//     {
//       'Chapter 1': 1,
//       'Chapter 2': 15,
//       'Chapter 3': 37,
//     },
//     10
//   )
// )

// ----------------------------------------------------------

// Moving Partition - edabit

// const movingPartition = (n) => {
//   let res = []

//   for (let i = 1; i < n.length; i++) {
//     res.push([n.slice(0, i), n.slice(i)])
//   }

//   return res
// }

// console.log(movingPartition([-1, -1, -1, -1]))

// ---------------------------------------------------------

// Is this a Haiku - edabit

// const haiku = (str) => {
//   // Checks for all vowel, considers all consecutive vowels as one
//   const r1 = /[aeiouyAEIOUY]+[aeiyouAEIOUY]?/g
//   //Checks e, e's and es that do NOT have a preceding aeiouy
//   const r2 = /(?<=[a-z]*[aeiouyAEIOUY]+[a-z]+)(e|e's|es)(?= |,|\b)/g

//   const haiku = str.split('/')

//   let counts = []

//   for (i in haiku) {
//     counts.push(
//       haiku[i].match(r1).length -
//         (haiku[i].match(r2) != null ? haiku[i].match(r2).length : 0)
//     )
//   }
//   let syllables = [5, 7, 5]

//   for (i in counts) {
//     if (counts[i] != syllables[i]) {
//       return false
//     }
//   }

//   return true
// }

// haiku("New vids ev'ry day / Never skipped a single day / I'll see you in March")

// -----------------------------------------------------------------------

// 118. Pascals Triangle - leetcode

// const generate = (n) => {
//   let res = [[1]]

//   for (let i = 1; i < n; i++) {
//     let row = []

//     for (let x = 0; x <= i; x++) {
//       let n1 = x - 1 < 0 ? 0 : res[i - 1][x - 1]
//       let n2 = x > res[i - 1].length - 1 ? 0 : res[i - 1][x]
//       row.push(n1 + n2)
//     }

//     res.push(row)
//   }

//   return res
// }

// console.log(generate(5))

// --------------------------------------------------------------------

// Conway's Game of Life - edabit

// const gameofLife = (board) => {
//   const res = []
//   const adj = [
//     [1, 0],
//     [1, 1],
//     [0, 1],
//     [-1, 1],
//     [-1, 0],
//     [-1, -1],
//     [0, -1],
//     [1, -1],
//   ]
//   for (i in board) {
//     let sub = ''
//     for (j in board[i]) {
//       let count = 0
//       for (k in adj) {
//         let x = Number(j) + adj[k][0]
//         let y = Number(i) + adj[k][1]
//         if (x >= 0 && x < board[i].length && y >= 0 && y < board.length) {
//           if (board[y][x] == 1) {
//             count += 1
//           }
//         }
//       }
//       if (board[i][j] == 1) {
//         switch (true) {
//           case count <= 1:
//             sub += '░'
//             break
//           case count <= 3:
//             sub += '█'
//             break
//           case count >= 4:
//             sub += '░'
//         }
//       } else {
//         if (count == 3) {
//           sub += '█'
//         } else {
//           sub += '░'
//         }
//       }
//     }
//     res.push(sub)
//   }0
//   return res.join('\n')
// }

// console.log(
//   gameofLife([
//     [0, 1, 0],
//     [1, 1, 1],
//     [0, 1, 0],
//   ])
// )

// ------------------------------------------------------

// Promises VIII: Old Callback API - edabit

// function saySomething(str) {
//   throw 'what the heck'
// }

// let ERR = ''

// const wait = () => new Promise((resolve, reject) => setTimeout(resolve, 1000))

// wait()
//   .then(() => saySomething('1 second has passed'))
//   .catch((err) => {
//     ERR = err
//   })

// ---------------------------------------------------

// Promises VII: Chaining - edabit

// function doSomething(isGoingToResolve = true) {
//   return new Promise((resolve, reject) => {
//     if (isGoingToResolve) {
//       resolve('something')
//     } else {
//       reject('something else')
//     }
//   })
//     .then((response) => {
//       console.log('in my function', response)
//       return response
//     })
//     .catch((error) => {
//       console.log('in my function', error)
//     })
// }

// doSomething().then((response) => {
//   console.log('in my main call', response)
// })

// ---------------------------------------------

// Recursion: Pronic Number - edabit

// const isHeteromecic = (n, i = 0) => {
//   let num = i * (i + 1)

//   if (num > n) {
//     return false
//   }

//   if (num == n) {
//     return true
//   }

//   return isHeteromecic(n, i + 1)
// }

// console.log(isHeteromecic(0))

// -----------------------------------------------------

// Super Reducing String - edabit

// const superReducingString = (str) => {
//   const regex = /([a-z])\1/

//   if (regex.test(str)) {
//     return superReducingString(str.replace(regex, ''))
//   }

//   if (str == '') {
//     return 'Empty String'
//   } else {
//     return str
//   }
// }

// console.log(superReducingString('abccdddd'))

// --------------------------------------------------------

// Look-and-Say Sequence - edabit

// const lookAndSay = (start, n) => {
//   let num = String(start)

//   let res = [start]

//   const regex = /([0-9])\1*/g

//   for (let i = 0; i < n - 1; i++) {
//     let nums = num.match(regex)

//     let sub = ''

//     for (let x = 0; x < nums.length; x++) {
//       sub += String(nums[x].length) + nums[x][0]
//     }

//     res.push(Number(sub))

//     num = sub
//   }

//   return res
// }

// console.log(lookAndSay(1, 7))

// -----------------------------------------------------------

// 119. Pascal's Triangle II - leetcode

// const generate = (rowIndex) => {
//   let res = [1]

//   for (let i = 1; i <= rowIndex; i++) {
//     let row = []

//     for (let x = 0; x <= i; x++) {
//       let n1 = x - 1 < 0 ? 0 : res[x - 1]
//       let n2 = x > res.length - 1 ? 0 : res[x]
//       row.push(n1 + n2)
//     }

//     res = row
//   }

//   return res
// }

// console.log(generate(3))

// --------------------------------------------------------

// Dead End Number Sequence

// Need to use BigInt() to deal with large values

const deadEnds = (n) => {
  let sequence = [n]

  const sumNums = String(n)
    .split('')
    .reduce((a, b) => {
      return Number(a) + Number(b)
    })

  while (true) {
    if (
      sequence[sequence.length - 1] == sequence[sequence.length - 3] ||
      sequence[sequence.length - 1] == sequence[sequence.length - 2]
    ) {
      return [
        Number(sequence.length) - 1,
        Number(sequence[sequence.length - 2]),
      ]
    }
    let num = BigInt(sequence[sequence.length - 1])

    const sumNums = BigInt(
      String(num)
        .split('')
        .reduce((a, b) => {
          return Number(a) + Number(b)
        })
    )
    if (num % sumNums == 0) {
      sequence.push(num / sumNums)
    } else {
      sequence.push(num * sumNums)
    }
  }
}

console.log(deadEnds(1))
