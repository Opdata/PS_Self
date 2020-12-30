# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []

        while head != None:
            val = head.val
            arr.append(val)
            head = head.next
        if arr == arr[::-1]:
            return True

        return False

node1 = ListNode(1);
node2 = ListNode(2);
node3 = ListNode(3);
node4 = ListNode(2);
node5 = ListNode(1);

node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;

f = Solution()
f.isPalindrome(node1)

# 다른 개선 풀이 1. List에 복사하고 pop 하면서 값을 비교할 수도 있다.
# 다른 개선 풀이 2. Deque 를 사용하여 pop 보다 빠른 속도로 값을 비교 할 수 있다.

# 최적 풀이 다른 자료형을 사용하지 않고 연결 리스트에서 풀이
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         rev = None
#         slow = fast = head
#
#         while fast and fast.next:
#             fast = fast.next.next
#             rev, rev.next, slow = slow, rev, slow.next
#
#         if fast:
#             slow = slow.next
#
#         while rev and rev.val == slow.val:
#             slow, rev = slow.next, rev.next
#
#         return not rev
