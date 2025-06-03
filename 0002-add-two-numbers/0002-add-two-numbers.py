# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0
        curr1 = l1
        curr2 = l2

        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0  # In case one of them has ended and val is 0
            val2 = curr2.val if curr2 else 0

            # Calculating quotient and carry:

            quotient = (carry + val1 + val2) % 10
            carry = (carry + val1 + val2) // 10

            curr.next = ListNode(quotient)

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            
            curr = curr.next

        if carry != 0:
            curr.next = ListNode(carry)
            curr = curr.next
        
        return dummy.next








        