class Solution:
    def sortArray(self, nums):
        """
        1. traverse the array of items
            1.1 traverse the array looking for the minimum 
            1.2 set new minimum if current minimum > current value
            1.3. swap current minimum with current item

        O(N^2) Runtime
        """
        new_array = nums

        for i in range(0, len(new_array)):
            iMin = i

            for j in range(i+1,  len(new_array)):
                if new_array[j] < new_array[iMin]:
                    iMin = j

            if iMin != i:
                minValue = new_array[iMin]
                iValue = new_array[i]

                new_array[i] = minValue
                new_array[iMin] = iValue

        return new_array


arr1 = [5,2,3,1]
arr2 = [5,1,1,2,0,0]
arr3 = [0,8,6,2,5,3,1,7]
solution = Solution()

print(solution.sortArray(arr3))