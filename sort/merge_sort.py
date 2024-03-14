class Solution():

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) <= 1:
            return nums

        left_half, right_half = self.splitArray(nums)

        left = self.sortArray(left_half)
        right = self.sortArray(right_half)

        return self.mergeArrays(left, right)

    def splitArray(self, nums):

        mid = len(nums) // 2

        left = []
        right = []

        for i in range(0, len(nums)):
            if i < mid:
                left.append(nums[i])
            else:
                right.append(nums[i])
        return left, right

    def mergeArrays(self, left, right):
        ileft = 0
        iright = 0
        newArray = []

        while ileft < len(left) and iright < len(right):
            if left[ileft] < right[iright]:
                newArray.append(left[ileft])
                ileft += 1
            else:
                newArray.append(right[iright])
                iright += 1

        while ileft < len(left):
            newArray.append(left[ileft])
            ileft += 1

        while iright < len(right):
            newArray.append(right[iright])
            iright += 1

        return newArray



arr1 = [5, 1, 1, 2, 0, 0]
solution = Solution()
print(solution.sortArray(arr1))
