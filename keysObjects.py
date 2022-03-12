
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    
        hashMap = {}

        def r(node):

            if node == None:
                return None

            n = Node(node.val)
            # YOU CAN USE OBJECTS IN DICT KEYS
            hashMap[node] = n

            n.next = r(node.next)

            if node.random:
                n.random = hashMap[node.random]
            else:
                n.random = None

            return n

        return r(head)