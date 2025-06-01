# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if k==0 or not head:
            return head

        length=0
        tail = None
        curr = head

        while curr:
            length += 1
            tail = curr
            curr = curr.next
        
        tail.next = head

        k=k%length

        back=None
        check=head
        for i in range(length-k):
            back=check
            check=check.next

        back.next=None

        return check



        

        


