# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        def merge(left, right):
            head = ListNode(0)
            curr = head
            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            
            if not left:
                curr.next = right
            
            if not right:
                curr.next = left
            
            return head.next

        def mergeSort(lists, l, r):
            if l > r:
                return lists
            
            if l == r:
                return lists[l]
            
            mid = l + (r - l)//2
            left = mergeSort(lists, l, mid)
            right = mergeSort(lists, mid + 1, r)
            return merge(left, right)
        
        if not lists:
            return None
        
        return mergeSort(lists, 0, len(lists) - 1)

        