# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node0 = ListNode()
        curr = node0
        p1, p2 = list1, list2

        while p1 and p2:
            val1 = p1.val
            val2 = p2.val
            if val1 <= val2:
                curr.next = p1
                p1 = p1.next
            elif val2 < val1:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        
        curr.next = p1 or p2
        return node0.next
        