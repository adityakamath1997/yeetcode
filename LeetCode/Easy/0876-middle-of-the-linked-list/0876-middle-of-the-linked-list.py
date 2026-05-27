# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        num_nodes = 0
        curr = head

        while curr:
            num_nodes += 1
            curr = curr.next

        count = (num_nodes // 2) + 1

        curr = head

        for i in range(count - 1):
            curr = curr.next

        return curr
        