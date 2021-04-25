
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
#from leetcode234 import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        dummy = result
        while l1 is not None and l2 is not None:
            if (l1.val < l2.val):
                newNode = ListNode(l1.val, l1.next)
                result.next = newNode
                result = newNode
                l1 = l1.next
            else:
                newNode = ListNode(l2.val, l2.next)
                result.next = newNode
                result = newNode
                l2 = l2.next
        while l1 is not None:
            newNode = ListNode(l1.val, l1.next)
            result.next = newNode
            result = newNode
            l1 = l1.next
        while l2 is not None:
            newNode = ListNode(l2.val, l2.next)
            result.next = newNode
            result = newNode
            l2 = l2.next
        return dummy.next


