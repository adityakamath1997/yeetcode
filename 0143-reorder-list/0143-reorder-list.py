# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        S = F = head

        while F and F.next:
            S = S.next
            F = F.next.next

        prev = None
        curr = S
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        left = head
        right = prev

        while right.next:
            tmp1 = left.next
            tmp2 = right.next
            left.next = right
            right.next = tmp1
            left = tmp1
            right = tmp2
