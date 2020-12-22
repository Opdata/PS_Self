# input = [7,1,5,3,6,4]
# input = [7,6,5,4,3,2,1]
# input = [2,4,1]
# input = [2,4,1,3]
# input = [1,6,1,5]
# input = [2,2]
# input = [2,1,2,1,0,1,2]
input = [4,7,2,1]

import sys

class Solution:
    def maxProfit(self, prices: list) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

f = Solution()
f.maxProfit(input)
