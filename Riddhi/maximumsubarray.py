class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSum = -10000000

        for i in range(len(nums)):
            sum += nums[i]

            if sum > maxSum:
                maxSum = sum

            if sum < 0:
                sum = 0

        return maxSum
