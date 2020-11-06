text = "A man, a plan, a canal: Panama"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = []
        str2 = []
        for char in s:
            if char.isalnum():
                str1.append(char.lower())

        for index in range(len(s) - 1, -1, -1):
            if s[index].isalnum():
                str1.append(s[index].lower())

        for index in range(0, len(str2)):
            if str1[index] != str2[index]:
                return False
        return True

# 개선1
#     def isPalindrome(self, s: str) -> bool:
#         str = []
#         for char in s:
#             if char.isalnum():
#                 str.append(char.lower())
#         while len(str) > 1:
#             if str.pop(0) != str.pop():
#                 return False
#         return True


# 개선2
#     def isPalindrome(self, s: str) -> bool:
#         # Deque 선언
#         strs: Deque = collection.deque()
#
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
#
#         return True

# 개선3
# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         # 정규식으로 불필요한 문자 필터링
#         s = re.sub('[^a-z0-9]', '', s)
#         return s == s[::-1]

f = Solution()
f.isPalindrome(text)