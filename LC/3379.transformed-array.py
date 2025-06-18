#
# @lc app=leetcode id=3379 lang=python3
#
# [3379] Transformed Array
#

# @lc code=start
class Solution:
    from typing import List
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            if nums[i] == 0:
                result[i] = nums[i]
            elif nums[i] > 0:
                result[i] = nums[(i + nums[i]) % n]
            else:
                result[i] = nums[(i - abs(nums[i])) % n]
        return result
# @lc code=end
if __name__ == "__main__":
    nums = [3,-2,1,1]  # Output: [1, 1, 1, 3]
    solution = Solution()
    print(solution.constructTransformedArray(nums))  
    nums = [-1,4,-1] # Output: [-1,-1,4]
    print(solution.constructTransformedArray(nums)) 
    nums = [0, 0, 0, 0]
    print(solution.constructTransformedArray(nums))  
