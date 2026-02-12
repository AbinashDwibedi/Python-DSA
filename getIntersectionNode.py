# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB) :

        # p1 = headA
        # p2 = headB
        # while p1 is not p2:
        #     p1 = p1.next if p1 else headB
        #     p2 = p2.next if p2 else headA
        # return p1

        visited = set()
        temp = headA
        while temp:
            visited.add(temp)
            temp = temp.next
        temp = headB
        while temp:
            if temp in visited:
                return temp
            temp = temp.next
        return None
        