class Solution:
    def sortArray(self, nums):
        """
        1. traverse the array of items
            1.1 traverse the array compare nums[i] and nums[i+1] 
            1.2 if nums[i] > nums[i+1] swap items
            1.3. elif nums[i] < nums[i+1] break;

        O(N^2) Runtime
        """
        new_array = nums

        for _ in range(0, len(new_array)):
            for j in range(0, len(new_array)-1):
                if new_array[j] > new_array[j+1]:
                    left = new_array[j]
                    right = new_array[j + 1]

                    new_array[j] =  right
                    new_array[j + 1] = left

        return new_array


arr1 = [5,2,3,1]
arr2 = [5,1,1,2,0,0]
arr3 = [0,8,6,2,5,3,1,7]
solution = Solution()

print(solution.sortArray(arr2))