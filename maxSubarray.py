class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = -10**5
        currSum = 0
        for num in nums:
            currSum += num
            if currSum > maxSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
        return maxSum 

        """
        maxSum is just initialized to a number that is smaller than the minimum possible
        element in nums so that it is always changed. currSum is added to num and maxSum becomes
        currSum if currSum is bigger. For me, the hardest part was figuring out that currSum 
        needs to be made zero if it's negative. If the next element is positive while currSum < 0,
        then you know the maxSubarray doesn't include anything before that point so currSum can become
        zero. If the next element is negative while currSum < 0, currSum is going to decrease anyway 
        so it's best to make it zero (while first keeping track of the actual maxSum BEFOREHAND) incase
        that next element is still bigger than currSum.
        """
        
