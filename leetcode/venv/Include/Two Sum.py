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
                
# 개선 target - n 값을 리스트에서 찾기
# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#         for i,n in enumerate(nums):
#             complement = target - n
#
#             if complement in nums[i + 1:]:
#                 return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

# 개선 키와 값을 바꿔서 dict 에 저장 후 찾기 ( 검색 속도 개선)
# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#         nums_map = {}
#
#         for i, num in enumerate(nums):
#             nums_map[num] = i
#
#         for i, num in enumerate(nums):
#             if target - num in nums_map and i != nums_map[target - num]:
#                 return nums.index(num), nums_map[target - num]


f = Solution()
f.twoSum(input, target)
