import sys

class Solution:
    """
    Find the Longest substring length with K Dinstict Character
    [A, A, A, H, H, I, B, C]
    O(n)
    """
    def longestSubStrLength(self, arr, k):
        distictCharCount = sys.maxsize
        windowStart = 0
        dict = {}

        for windowEnd in range(0, len(arr)):
            currentChar = arr[windowEnd]

            if currentChar in dict : dict[currentChar] += 1
            else: dict[currentChar] = 1

            if len(dict) >= (k + 1):
                charAtWindowStart = arr[windowStart]
                dict[charAtWindowStart] -=1
                distictCharCount = min(distictCharCount, (windowEnd - windowStart) + 1)
                windowStart += 1

            print(dict)



        return distictCharCount
    
solution = Solution()
arr1 = ["A", 'A', 'A', 'H', 'H', 'I', 'B', 'C']
# arr2 = [5,4,-1,7,8]
# arr3 = [-2,1,-3,4,-1,2,1,-5,4]

print(solution.longestSubStrLength(arr1, 2))