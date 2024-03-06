class Solution:
    """
    Find the Longest substring without Repeating Character
    pwwkew
    O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        distinctCharLen = 0
        windowStart = 0

        for windowEnd, char in enumerate(s):

            # distinctCharLen += 1

            while char in dict:
                del dict[char]

            if char not in  dict: dict[char] = 1
  
        print(dict)
        return len(dict)
       


solution = Solution()
str1 = "abcabcbb"
str2 = "bbbbb"
str3 = "pwwkew"

print(solution.lengthOfLongestSubstring(str3))