# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        seen = []
        curr = head

        while curr:
            seen.append(curr.val)
            curr = curr.next

        seen.sort()
        dummy = ListNode()
        curr = dummy

        for i in seen:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next
        