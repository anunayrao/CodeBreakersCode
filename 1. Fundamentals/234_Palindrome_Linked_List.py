# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        '''
        Pseudocode:
        1. Assign the dummy node to the list for easier manipulation.
        2. Now maintain two pointers namely, fast and slow both pointing to the dummy node of
           the list initially. The fast pointer will advance at twice the speed of the slow              pointer.
        3.As the fast pointer will reach to the end of the list slow pointer will be in the             middle. Now Two cases arise:
        4. Now just save the next pointer of the slow namely, second_half and reverse it.
        5. Now  we can Simultaneously advance the first_half pointer pointing to the head of the list and the second_half to compare whether the list ispalindrome or not. 
           
        '''
        if head is None or head.next is None:
            return True
        
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        
        
        first_half = head
    
        
        slow = slow.next
        second_half = self.reverse(slow)
            
        
        
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True
    
    def reverse(self, head):
        
        curr = head
        prev = None
        
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
        return prev
        
        
        
        
        