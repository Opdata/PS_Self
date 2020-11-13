input = "babad"
# input = "cbbd"
# input = "a"
# input = "ac"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        for left in range(0,len(s)):
            for right in range(len(s)-1,left-1,-1):
                if len(s) == 2 and s[left] != s[right]:
                    return s[left]
                if s[left] == s[right]:
                    midIndex = (left+right)//2
                    leftList = s[left:midIndex+1]
                    rightList = s[midIndex+1:left:-1]
                    if leftList == rightList:
                        return s[left:right+1]

# 개선, 간단한 예외처리 및 여러개의 팰린드롬이 나오면 길이가 최대인것을 반환
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # 팰린드롬 판별 및 투 포인터 확장
#         def expand(left:int, right:int) -> str:
#             while left >= 0 and right <= len(s) and s[left] == s[right-1]:
#                 left -= 1
#                 right += 1
#                 return s[left + 1:right - 1]
#         if len(s) < 2 or s == s[::-1]:
#             return s
#         result = ''
#     # 슬라이딩 윈도우 우측으로 이동
#         for i in range(len(s) - 1):
#             result = max(result,expand(i, i + 1), expand(i, i + 2), key=len)
#         return result

f = Solution()
f.longestPalindrome(input)