class Solution:
    """abcdefgh
    Find the Longest substring without Repeating Character
    abcabcbb
    O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        distinctCharLen = 0
        windowStart = 0

        for windowEnd, char in enumerate(s):

            while char in my_dict:
                del my_dict[s[windowStart]]
                windowStart += 1

            if char not in my_dict:
                my_dict[char] = 1
                distinctCharLen = max(distinctCharLen, (windowEnd - windowStart) + 1)

        return distinctCharLen
       


solution = Solution()
str1 = "abcabcbb"
str2 = "bbbbb"
str3 = "pwwkew"

print(solution.lengthOfLongestSubstring(str3))
