# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        slow = fast = head
        slow2=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            
            if fast==slow:
                break
        
        if not fast.next or not fast.next.next:
            return 
        
        while slow.next:
            if slow==slow2:
                return slow
            else:
                slow=slow.next
                slow2=slow2.next
        
        return


        