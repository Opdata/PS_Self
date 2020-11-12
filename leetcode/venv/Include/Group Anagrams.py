input = ["eat","tea","tan","ate","nat","bat"]

import collections

class Solution:
    def groupAnagrams(self, strs) -> list:
        emptyDict = collections.defaultdict(list)
        for i in strs:
            emptyDict[''.join(sorted(i))].append(i)
        return emptyDict.values()

f = Solution()
f.groupAnagrams(input)



#[
# ["ate","eat","tea"],
# ["nat","tan"],
# ["bat"]
# ]