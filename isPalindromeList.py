# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        numbers = ""
        temp = head
        while temp != None:
            numbers += str(temp.val)
            temp = temp.next
        return numbers == "".join(reversed(numbers))
            