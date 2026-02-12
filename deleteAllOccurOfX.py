
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        temp = head
        while temp:
            nxt = temp.next
            if temp.data == x:
                if temp.prev is None:
                    head = temp.next
                    if head:
                        head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
            temp = nxt
        return head
