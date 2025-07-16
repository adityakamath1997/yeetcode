# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def get_length(head):
            curr = head
            length = 0
            while curr:
                length += 1
                curr = curr.next
            return length

        length = get_length(head)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        for i in range(length // 2):
            temp = curr.next
            prev.next = temp
            curr.next = temp.next
            temp.next = curr

            prev = curr
            curr = curr.next

        return dummy.next
