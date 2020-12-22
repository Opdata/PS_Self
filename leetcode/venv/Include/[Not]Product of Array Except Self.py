input = [1,2,3,4]

class Solution:
    def productExceptSelf(self, nums: list) -> list:
        p = 1
        out = []
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]

        p = 1

        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p *= nums[i]

        return out

f = Solution()
f.productExceptSelf(input)