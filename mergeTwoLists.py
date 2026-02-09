# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        nxt = dummy
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                nxt.next = ListNode(list1.val)
                list1 = list1.next
            else:
                nxt.next = ListNode(list2.val)
                list2 = list2.next
            nxt = nxt.next
        while list1 != None:
            nxt.next = ListNode(list1.val)
            nxt = nxt.next
            list1 = list1.next
        while list2 != None:
            nxt.next = ListNode(list2.val)
            nxt = nxt.next
            list2 = list2.next
        return dummy.next