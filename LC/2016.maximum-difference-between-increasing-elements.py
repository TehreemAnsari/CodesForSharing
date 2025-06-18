#
# @lc app=leetcode id=2016 lang=python3
#
# [2016] Maximum Difference Between Increasing Elements
#

# @lc code=start
class Solution:
    from typing import List
    def maximumDifference(self, nums: List[int]) -> int:
        left, right, max_diff = 0, 1, -1

        while right < len(nums):
            if nums[left] < nums[right]:
                max_diff = max(max_diff, nums[right] - nums[left])
            else:
                left = right
            right += 1
        return max_diff 
# @lc code=end

if __name__ == "__main__":
    nums = [7, 1, 5, 4]
    solution = Solution()
    print(solution.maximumDifference(nums))  # Output: 4
    nums = [9, 4, 3, 2]
    print(solution.maximumDifference(nums))  # Output: -1
    nums = [1, 5, 2, 10]
    print(solution.maximumDifference(nums))  # Output: 9