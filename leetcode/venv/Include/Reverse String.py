List = ["H","a","n","n","a","h"]

class Solution:
    def reverseString(self, s) -> None:
        left, right = 0, len(s) - 1
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# 개선1
# class Solution:
#     def reverseString(self, s) -> None:
#         List[:] = s[::-1]

# 개선2
# class Solution:
#     def reverseString(self, s) -> None:
#         s.reverse()

f = Solution()
f.reverseString(List)
print(List)

