input, target = [2,7,11,15] , 9
# input, target = [3,2,4] , 6
# input, target = [3,3] , 6

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        if len(nums) == 2:
            return [0,1]
        lessNums = []
        for i in nums:
            if i < target:
                lessNums.append(i)
        for i in range(0, len(lessNums)):
            for j in range(i, len(lessNums)):
               if target == lessNums[i] + lessNums[j]:
                   return [i,j]


f = Solution()
f.twoSum(input, target)
