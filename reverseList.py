# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        # stack method 
        # if head == None:
        #     return head
        # stack = list()
        # temp = head
        # while temp != None:
        #     stack.append(temp.val)
        #     temp = temp.next
        # temp = head
        # while temp!=None:
        #     temp.val = stack.pop()
        #     temp = temp.next
        # return head 

        if head == None or head.next == None:
            return head
        prev = head
        nxt = head.next
        prev.next = None
        while nxt != None:
            tmp = nxt.next
            nxt.next = prev
            prev = nxt
            nxt = tmp
        head = prev
        return head