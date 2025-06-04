# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        dummy1 = ListNode()
        dummy2 = ListNode()
        curr1 = dummy1
        curr2 = dummy2
        curr = head

        while curr:
            if curr.val < x:
                curr1.next = curr
                curr1 = curr1.next
            elif curr.val >= x:
                curr2.next = curr
                curr2 = curr2.next
            curr = curr.next
        
        curr2.next = None
        curr1.next = dummy2.next

        return dummy1.next