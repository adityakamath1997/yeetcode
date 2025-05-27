# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        head=dummy

        while list1 and list2:
            val1 = list1.val 
            val2 = list2.val 

            if val1>=val2:
                head.next=list2
                list2=list2.next
            else:
                head.next=list1
                list1=list1.next
            head=head.next
        
        head.next= list1 or list2
            
            
        return dummy.next



        