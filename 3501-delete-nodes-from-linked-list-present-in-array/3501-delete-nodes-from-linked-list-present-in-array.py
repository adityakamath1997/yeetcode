# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        prev=dummy
        curr=head
        nums=set(nums)
        while curr:
            if curr.val in nums:
                prev.next=curr.next
                curr=curr.next
            else:
                prev=prev.next
                curr=curr.next

        return dummy.next