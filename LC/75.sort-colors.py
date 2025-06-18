#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    from typing import List
    def sortColors(self, nums: List[int]) -> None:
        """
        Also called Dutch National flag problem
        https://chatgpt.com/c/6851b1c6-8e80-800f-9416-101d568c4fdb
        full explaination why we are doing "i += 1" only in "nums[i] == 0 block"
        Do not return anything, modify nums in-place instead.
        inplace: Without extra space. This doesn't mean relative order is maintained. 
        When relative order is maintained, that is called "stable"
        
        #p is the pointer that will move 
        #left -> sliding window of left side, right -> right side window

        left: boundary for 0s (all values left of left are 0).
        right: boundary for 2s (all values right of right are 2).
        """
        left, right, i = 0, len(nums) - 1, 0

        while i <= right:
            if nums[i] == 0:
                # Swap current 0 with the value at the left boundary
                nums[i], nums[left] = nums[left], nums[i]
                # After this swap:
                #   nums[i] is now the old value of nums[left]
                #   But nums[left] was already processed, and is never 2
                #   So after this swap, nums[i] CANNOT be 2 ❌
                # It must be 0 or 1 → safe to move i forward
                left += 1
                i += 1

            elif nums[i] == 2:
                # Swap current 2 with the value at the right boundary
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                # Do NOT increment i here
                # The value that came from the right might be 0, 1, or 2
                # So we need to recheck the current nums[i]

            else:
                # nums[i] == 1 → nothing to do, just move on
                i += 1
            
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors(nums)
    print(nums)  # Output should be [0, 0, 1, 1, 2, 2]