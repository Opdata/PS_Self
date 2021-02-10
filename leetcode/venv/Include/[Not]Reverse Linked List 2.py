# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # Node.val 값을 이용한 풀이가 아닌 정석 연결리스트 풀이
        if not head or m == n:
            return head
        
        root = start = ListNode(None)
        root.next = head
        
        for _ in range(m - 1):
            start = start.next
        
        end = start.next
        
        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        
        return root.next