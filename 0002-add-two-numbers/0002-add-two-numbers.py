# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        curr1 = l1
        curr2 = l2
        carry = 0
        while curr1 or curr2:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0

            quotient = (carry + v1 + v2) % 10
            carry = (carry + v1 + v2) // 10

            curr.next = ListNode(quotient)
            curr = curr.next
            
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        
        if carry != 0:
            curr.next = ListNode(carry)
            curr = curr.next


        return dummy.next






        