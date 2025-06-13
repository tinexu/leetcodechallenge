class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        prefixSums = []
        currSum = 0
        for num in nums:
            currSum += num
            prefixSums.append(currSum)
        right = len(nums) - 1
        left = right - 1
        found = False
        smallestLength = 10**5 + 1
        while right > left and left >= 0:
            difference = prefixSums[right] - prefixSums[left]
            if difference < target:
                left -= 1
            if difference >= target:
                found = True
                smallestLength = min(smallestLength, right - left)
                right -= 1
        for i in range(len(prefixSums)):
            if prefixSums[i] >= target:
                if found:
                    return min(smallestLength, i + 1)
                return i + 1
        return 0
        
