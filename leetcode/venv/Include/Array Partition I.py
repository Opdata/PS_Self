input = [6,2,6,5,1,2]
# input = [1,4,3,2]

class Solution:
    def arrayPairSum(self, nums: list) -> int:
        nums.sort()
        sum = 0
        if len(nums) == 2:
            return nums[0]
        for i in nums[::2]:
            sum += i

        return sum

f = Solution()
f.arrayPairSum(input)