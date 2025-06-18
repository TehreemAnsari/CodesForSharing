#
# @lc app=leetcode id=3423 lang=python3
#
# [3423] Maximum Difference Between Adjacent Elements in a Circular Array
#

# @lc code=start
class Solution:
    from typing import List
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        for i in range(len(nums)):
            diff = abs(nums[i] - nums[(i+1) % len(nums)])
            max_diff = max(max_diff, diff)
        return max_diff
# @lc code=end
if __name__ == "__main__":
    nums = [1, 3, 2, 5, 4]
    solution = Solution()
    print(solution.maxAdjacentDistance(nums))  # Output: 3
    nums = [10, 20, 30, 40]
    print(solution.maxAdjacentDistance(nums))  # Output: 10
    nums = [1, 1, 1, 1]

