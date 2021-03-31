# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ptr = head
        number =0
        reverse_number=0
        while (ptr is not None):
            number = number*10+ptr.val
            ptr = ptr.next
        original_number = number
        reverse_list = self.reverse(self, head)
        while number > 0:
            reverse_number = int(reverse_number*10) + int(number%10)
            number = int(number/10)
        return self.areIdentical(self, head,reverse_list)

            # Returns true if linked lists a and b
            # are identical, otherwise false

    def areIdentical(self, lista, listb):
            a = lista
            b = listb
            while (a != None and b != None):
                if (a.val != b.val):
                    return False

                # If we reach here, then a and b
                # are not null and their data is
                # same, so move to next nodes
                # in both lists
                a = a.next
                b = b.next

            # If linked lists are identical,
            # then 'a' and 'b' must be null
            # at this point.
            return (a == None and b == None)

            # Function to reverse the linked list
    def reverse(self, head: ListNode):
        prev = None
        current = head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head

first = ListNode(1)
second = ListNode(3)
third = ListNode(3)
forth = ListNode(1)
first.next = second
second.next = third
third.next = forth
forth.next = None

solution = Solution
print(solution.isPalindrome(solution,first))