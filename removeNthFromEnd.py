# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        # count = 0
        # temp = head
        # while temp != None:
        #     count += 1
        #     temp = temp.next
        # goalNode = count- n
        # if goalNode == 0:
        #     head = head.next
        #     return head
        # temp = head 
        # count = 1
        # while count != goalNode:
        #     count += 1
        #     temp = temp.next
        # temp.next = temp.next.next
        # return head

        fast = head
        for i in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        slow = head
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head