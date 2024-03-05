import sys

class Solution:
    """
    Find the smallest size of sub-array with given sum
    [4, 2, 2, 7, 8, 1, 2, 8, 10]
    O(n)
    """
    def smallCountOfSubArrayGivenSum(self, arr, k):
        minWindowSize = sys.maxsize #largest represenattion of int
        currentWindowSum = 0
        windowStart = 0

        for windowEnd in range(0, len(arr)):
            currentWindowSum += arr[windowEnd]

            print("Before", arr[windowStart], arr[windowEnd],  windowEnd, windowStart, currentWindowSum, minWindowSize)
            while currentWindowSum >= k:
                minWindowSize = min(minWindowSize, (windowEnd - windowStart) + 1)
                currentWindowSum -= arr[windowStart]
                windowStart+=1
                print("After", currentWindowSum, minWindowSize, windowStart)

        return minWindowSize
    
solution = Solution()
arr1 = [4, 2, 2, 7, 8, 1, 2, 8, 10]
arr2 = [5,4,-1,7,8]
arr3 = [-2,1,-3,4,-1,2,1,-5,4]

print(solution.smallCountOfSubArrayGivenSum(arr1, 8))