#
# @lc app=leetcode id=3442 lang=python3
#
# [3442] Maximum Difference Between Even and Odd Frequency I
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        
        freq = Counter(s)
        odd = 0
        even = len(s)

        for count in freq.values():
            if count % 2 == 1:
                odd = max(odd, count)
            elif count != 0:
                even = min(even, count)

        return odd - even
# @lc code=end
if __name__ == "__main__":
    s = "aabbbcc"
    solution = Solution()
    print(solution.maxDifference(s))  # Output: 0
    s = "abcde"
    print(solution.maxDifference(s))  # Output: 5
    s = "aabbccddeeff"
    print(solution.maxDifference(s))  # Output: 0
