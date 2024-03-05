import sys

class Solution:
    """
    Find the max of the sum of subarray of fixed size k
    [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    O(n)
    """
    def findMaxSumOfSubArray(self, arr, k):
        maxValue = ~sys.maxsize #smallest represenattion of int
        currentSum = 0

        for i in range(0, len(arr)):
            currentSum += arr[i]

            if i >= k:
                currentSum -= arr[i-k]
                maxValue = max(currentSum, maxValue)

        return maxValue
    
solution = Solution()
arr1 = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
arr2 = [5,4,-1,7,8]
arr3 = [-2,1,-3,4,-1,2,1,-5,4]

print(solution.findMaxSumOfSubArray(arr2, 3))