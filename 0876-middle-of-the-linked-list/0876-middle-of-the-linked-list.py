# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None and head.next is None: 
            return head 
        length = 1 
        current = head 
        while current.next is not None :
            current = current.next 
            length +=1 
        middle = length //2 
        while middle : 
            head = head.next 
            middle -= 1 
        return head 
        