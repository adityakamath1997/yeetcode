# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            node = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10

            curr.next = ListNode(node)
            curr = curr.next

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        if carry != 0:
            curr.next = ListNode(carry)

        return dummy.next

        