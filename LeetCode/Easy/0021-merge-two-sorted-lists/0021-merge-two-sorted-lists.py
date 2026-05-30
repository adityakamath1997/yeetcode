# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        node = ListNode()
        head = node
        p1 = list1
        p2 = list2

        while p1 and p2:
            val1 = p1.val
            val2 = p2.val

            if val1 < val2:
                head.next = p1
                p1 = p1.next
            
            else:
                head.next = p2
                p2 = p2.next

            head = head.next

        head.next = p1 or p2

        return node.next
        