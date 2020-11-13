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

f = Solution()
f.longestPalindrome(input)