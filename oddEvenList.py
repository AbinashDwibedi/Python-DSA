# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        # lm method
        # oddPart = ListNode(0)
        # temp1 = oddPart
        # evenPart = ListNode(0)
        # temp2 = evenPart
        # i = 0
        # temp = head
        # while temp != None:
        #     if i % 2 == 0:
        #         temp1.next = ListNode(temp.val)
        #         temp1 = temp1.next
        #     else:
        #         temp2.next = ListNode(temp.val)
        #         temp2 = temp2.next
        #     i+=1
        #     temp = temp.next
        # temp1.next = evenPart.next
        # return oddPart.next
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
