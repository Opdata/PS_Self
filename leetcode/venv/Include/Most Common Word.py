paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        key_value = 0
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() # ^(not),\w(단어문자)
                 if word not in banned]
        count_words = collections.Counter(words)
        for key in count_words:
            if count_words[key] == max(count_words.values()):
                return key

# 개선
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: list) -> str:
#         key_value = 0
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() # ^(not),\w(단어문자)
#                  if word not in banned]
#         count_words = collections.Counter(words)
#         return count_words.most_common(1)[0][0]


f = Solution()
f.mostCommonWord(paragraph, banned)