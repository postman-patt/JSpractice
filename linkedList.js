// don't change this code
class Node {
  constructor(v) {
    this.val = v
    this.next = null
  }
}
class LinkedList {
  constructor(a) {
    this.head = null
    this.tail = null
    if (!!a) {
      a.forEach((v) => {
        this.insertTail(v)
      })
    }
  }
  insertHead(v) {
    let nn = new Node(v)
    nn.next = this.head
    if (!this.tail) {
      this.tail = nn
    }
    this.head = nn
  }
  insertTail(v) {
    if (!this.head) return this.insertHead(v)
    let nn = new Node(v)
    this.tail.next = nn
    this.tail = nn
  }
  print() {
    let o = [],
      node = this.head
    while (node) {
      o.push(node.val)
      node = node.next
    }
    return o
  }
}
// okay, you can change stuff below this line. Have fun!

const list1 = new LinkedList([1, 2, 3, 4, 5, 6])
const list2 = new LinkedList([8, 6, 7, 5, 3, 0, 9])
const list3 = new LinkedList([1, 1, 3, 8])
const list4 = new LinkedList(['a', 'b', 'c', 'e'])
const list5 = new LinkedList(['r', 'a', 'c', 'e', 'c', 'a', 'r'])
const list6 = new LinkedList([1])

const reverseLinkedList = (linkedlist) => {
  var current = linkedlist.head
  var next = null
  var temp_next = linkedlist.head.next
  while (true) {
    current.next = next
    // head.next = null | node2.next = head
    next = current
    // next = head |next = node2

    if (temp_next == null) {
      break
    }
    current = temp_next
    // current = node2 | current = node3

    temp_next = temp_next.next
    // temp_next = node3 | temp_next = node4
  }

  ;[linkedlist.head, linkedlist.tail] = [linkedlist.tail, linkedlist.head]

  return linkedlist.print()
}

console.log(reverseLinkedList(list6))
console.log(list6)
