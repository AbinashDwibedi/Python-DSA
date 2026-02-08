# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        while l1!=None or l2!=None:
            val1 = 0
            val2 = 0
            if l1!=None:
                val1 = l1.val
                l1 = l1.next
            if l2!=None:
                val2 = l2.val
                l2 = l2.next
            sumi = val1+val2+carry
            carry = sumi//10
            temp.next = ListNode(sumi%10)
            temp = temp.next
        if carry != 0:
            temp.next = ListNode(carry)
        return dummy.next
