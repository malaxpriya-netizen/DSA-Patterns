# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # Step 1: Determine if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they intersect, a cycle is confirmed
            if slow == fast:
                # Step 2: Find the entry point of the cycle
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next  # FIXED: Move fast by 1 step, not 2
                return slow
                
        # If the fast pointer reaches the end, there is no cycle
        return None
