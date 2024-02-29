class Solution:
    def sortArray(self, nums):
        """
        start from nums[1] because nums[0] does have a left
        compare the nums[1] with nums[0], if nums[0] > nums[1]
        swap nums[0] , nums[1]
        O(N^2) Runtime
        """
        new_array = nums

        last_index = len(new_array) - 1

        for i in range(0, last_index):

            j = i + 1
            
            while j > 0 and new_array[j - 1] > new_array[j]: 
                left_num = new_array[j - 1]
                current_num = new_array[j]
     
                new_array[j - 1] = current_num
                new_array[j] = left_num

                j -=1

        return new_array


arr1 = [5,2,3,1]
arr2 = [5,1,1,2,0,0]
solution = Solution()

print(solution.sortArray(arr2))