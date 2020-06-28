# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # Pseudocode:
        #1. If the list is Empty or the value of n is <=0 or n> lenght of list then return None
        #2. Assign a dummy node to the head of the list for easier manipulation. Maintain 2 pointers namely, ahead, behind. ahead and behind pointing to head of the list initially.
        #3. Advance ahead pointer by n+1 so now the gap between ahead and behind pointer is n+1. 
        #4. Now advance both ahead and behind pointer simulatenously.
        #5. Now as the ahead pointer reaches to the end of the list behind pointer points to node previous to the node to be removed which can now be removed easily. 
        
        if head is None or n<=0:
            return None
        
        if n==1 and head.next is None:
            head = None
            return head
        dummy = ListNode(0)
        dummy.next = head
        
        ahead = dummy
        behind = dummy 
       
        
        while n>=0:
            ahead = ahead.next
            n -= 1
        
        while ahead:
            behind = behind.next
            ahead = ahead.next
            
        behind.next = behind.next.next
        
        return dummy.next