class Solution:
    """
    Find the middle node of the linked list
    [1,2,3,4,5]
    O(n)
    """

    def middleNode(self, head):

        slow_pointer = head
        fast_pointer = head


        while fast_pointer is not None and fast_pointer.next is not None: 

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next


        return slow_pointer


solution = Solution()
arr1 = [1, 2, 3, 4, 5]

print(solution.longestSubStrLength(arr1, 1))
