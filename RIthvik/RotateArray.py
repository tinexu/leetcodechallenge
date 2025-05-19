class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rotatedNums = []
        for i in range(len(nums)):
            rotatedNums.append(1)
        for i in range(len(nums)):
            newIndex = (i + k) % len(nums)
            rotatedNums[newIndex] = nums[i]
        for i in range(len(rotatedNums)):
            nums[i] = rotatedNums[i]
        
