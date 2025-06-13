class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        currSum = 0
        maxSum = -10**9
        for i in range(k):
            currSum += nums[i]
        maxSum = max(currSum, maxSum)
        left = 0
        right = k - 1
        while right < len(nums) - 1:
            currSum -= nums[left]
            left += 1
            right += 1
            currSum += nums[right]
            maxSum = max(currSum, maxSum)
        return (maxSum * 1.0) / k
