# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        #PseudoCode:
        # 1. Find the length of both the linked list. 
        # 2. Advance the head of the longer linked list by the difference of their lengths.
        # 3. Now advance both the linked list untill intersection is found or the end of either of the linked list is reached in which case return None as Intersection is not found
        
        if headA is None or headB is None:
            return None
        if headA is headB:
            return headA
        
        length1 = 0 
        length2 = 0
        head1 = headA
        head2 = headB
        
        while head1:
            length1 += 1
            head1 = head1.next
            
        while head2:
            length2 += 1
            head2 = head2.next
            
        if length2 > length1:
            headA , headB = headB, headA
            
        diff = abs(length1 - length2)
        
        curr = headA
        
        while diff > 0:
            curr = curr.next
            diff -= 1
            
        while curr:
            if curr is headB:
                return curr
            curr = curr.next
            headB = headB.next
        
        return None
            
        