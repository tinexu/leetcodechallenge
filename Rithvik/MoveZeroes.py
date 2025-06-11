class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        currIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[currIndex]
                nums[currIndex] = temp
                currIndex += 1


"""
This finishes in O(n) time because it's just one for-loop
and its time complexity is O(1) becasue regardless of the size
of nums, the only new variables are the integers currIndex and 
temp
"""
