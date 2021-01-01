# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1

node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(4)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

f = Solution()
f.mergeTwoLists(node1, node2)