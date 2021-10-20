//Basic Javascript hashMap

const groupAnagrams = (arr) => {
  const hashMap = new Map()

  for (i in arr) {
    let sortStr = arr[i].split('').sort().join('')
    if (hashMap.has(sortStr)) {
      hashMap.set(sortStr, [...hashMap.get(sortStr), arr[i]])
    } else {
      hashMap.set(sortStr, [arr[i]])
    }
  }

  return Array.from(hashMap.values())
}

console.log(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
console.log(groupAnagrams(['']))
console.log(groupAnagrams(['', '', '']))
