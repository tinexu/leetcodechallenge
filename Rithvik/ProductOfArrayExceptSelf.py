class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftProducts = [1]
        for i in range(1, len(nums)):
            leftProducts.append(leftProducts[i - 1] * nums[i - 1])
        rightProducts = []
        for num in nums:
            rightProducts.append(1)
        for i in range(len(nums) - 2, -1, -1):
            rightProducts[i] = rightProducts[i + 1] * nums[i + 1]
        answers = []
        for i in range(len(nums)):
            answers.append(rightProducts[i] * leftProducts[i])
        return answers

"""
This solution is legit ass because I'm stupid. It uses two additional arrays 
of length n, making the space complexity 2n...and it uses FOUR loops whose 
lengths are each either n - 1 or n, making the time complexity approximately 4n.
"""
