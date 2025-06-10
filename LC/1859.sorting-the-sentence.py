#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        list_of_words = s.split()
        sorted_words = sorted(list_of_words, key=lambda x: int(x[-1]))
        sorted_sentence = ' '.join(word[:-1] for word in sorted_words)
        return sorted_sentence
# @lc code=end
# if __name__ == "__main__":
#     # Example usage
#     s = "is2 sentence4 This1 a3"
#     solution = Solution()
#     result = solution.sortSentence(s)
#     print(result)  # Output: "This is a sentence"
# # Example usage
#     s = "Myself2 Me1 I4 and3"
#     solution = Solution()
#     result = solution.sortSentence(s)
#     print(result)  # Output: "Me Myself and I"
