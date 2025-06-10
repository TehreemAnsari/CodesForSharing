#
# @lc app=leetcode id=1061 lang=python3
#
# [1061] Lexicographically Smallest Equivalent String
#

# @lc code=start
class Solution:
    def smallestEquivalentString(self, s1, s2, baseStr):
        parent = list(range(26))  # For 'a' to 'z'

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        # Union step: group all equivalent characters
        for i, j in zip(s1, s2):
            x, y = ord(i) - ord('a'), ord(j) - ord('a')
            px, py = find(x), find(y)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        # Build the result
        result = []
        for c in baseStr:
            idx = ord(c) - ord('a')
            root = find(idx)
            smallest = chr(root + ord('a'))
            print(f"Character '{c}' -> root '{smallest}'")  # Debug output
            result.append(smallest)
        return ''.join(result)

if __name__ == "__main__":
    # Example usage
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    sol = Solution() # Create an instance of the Solution class
    answer = sol.smallestEquivalentString(s1, s2, baseStr) # Call the method
    print("Final answer:", answer)

# @lc code=end

