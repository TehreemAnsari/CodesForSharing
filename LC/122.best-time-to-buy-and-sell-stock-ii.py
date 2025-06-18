#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    from typing import List
    def maxProfit(self, prices: List[int]) -> int:
        left, right, profit = 0, 1, 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit += prices[right] - prices[left]
            left += 1
            right += 1
        return profit
# @lc code=end
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maxProfit(prices))  # Output: 7
    prices = [1, 2, 3, 4, 5]
    print(solution.maxProfit(prices))  # Output: 4
    prices = [7, 6, 4, 3, 1]
    print(solution.maxProfit(prices))  # Output: 0