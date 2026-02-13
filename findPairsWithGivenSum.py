from typing import Optional


from typing import List


# Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

# You can also use the following for printing the link list.
# displayList(node)
class Solution:
    def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
        result = []
        left = head
        right = head
        while right.next:
            right = right.next
        
        while left.data < right.data:
            sumi = left.data + right.data 
            if sumi == target:
                result.append([left.data,right.data])
                left = left.next
                right = right.prev
            elif sumi > target:
                right = right.prev
            else:
                left = left.next
        return result

