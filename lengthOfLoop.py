
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None


class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow = head
        fast = head
        count = 0
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next
            if slow == fast :
                break
        else:
            return 0
        
        count += 1
        temp = slow.next
        while temp != slow:
            temp = temp.next
            count +=1 
        return count
        
        