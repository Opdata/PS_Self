input = [-1,0,1,2,-1,-4]
# input = []
# input = [0]

class Solution:
    def threeSum(self, nums: list) -> list:
        if len(nums) < 3:
            return []

        result = []
        nums.sort()
        data = []

        for i in range(len(nums)):
            test = []
            sum = 0

            for j in range(i+1,len(nums)):
              if nums[i] <= nums[j]:
                  test.append(nums[j])

            for k in range(len(test)):

                sum = nums[i] + test[k]
                for h in range(k+1,len(test)):

                    if (test[h] + sum) == 0:
                        data = [nums[i],test[k],test[h]]
                        data.sort()

                    if len(result) == 0 and len(data) != 0:
                        result.append(data)
                        data = []

        for arr in result:
            if arr != data and len(data) != 0:
                result.append(data)
                data = []

        return result

f = Solution()
f.threeSum(input)
