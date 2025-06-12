from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seenSums = defaultdict(int)
        count = 0
        currSum = 0
        for num in nums:
            currSum += num
            if currSum == k:
                count += 1
            complement = currSum - k
            if complement in seenSums:
                count += seenSums[complement]
            seenSums[currSum] += 1
        return count
