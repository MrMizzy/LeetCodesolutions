# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        slow_point = head
        fast_point = head

        while fast_point is not None and fast_point.next is not None:
            slow_point = slow_point.next
            fast_point = fast_point.next.next

        return slow_point