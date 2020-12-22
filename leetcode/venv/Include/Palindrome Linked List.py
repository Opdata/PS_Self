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

# List에 복사하고 pop 하면서 값을 비교할 수도 있다.
# Deque 를 사용하여 pop 보다 빠른 속도로 값을 비교 할 수 있다.
