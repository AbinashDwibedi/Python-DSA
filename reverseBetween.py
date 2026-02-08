# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):

        start = head
        count = 0
        while count != left-1:
            start = start.next
            count +=1
        stack = list()
        temp = start
        for i in range(left,right+1):
            stack.append(temp.val)
            temp = temp.next
        temp = start
        for i in range(left,right+1):
            temp.val = stack.pop()
            temp = temp.next
        return head