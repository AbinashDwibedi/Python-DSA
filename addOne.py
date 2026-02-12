
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        
        def helper(head):
            if not head:
                return 1
            carry = helper(head.next)
            sumVal = carry + head.data
            head.data  = sumVal % 10
            return sumVal // 10
        carry = helper(head)
        if carry > 0:
            dummy = Node(carry)
            dummy.next = head
            head = dummy
        return head