def createInterval(num1, num2):
    if num1 == num2:
        return str(num1)
    return str(num1)+"->"+str(num2)
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [createInterval(nums[0], nums[0])]
        startNum = nums[0]
        prevNum = nums[0]
        endNum = nums[0]
        ranges = []
        currIndex = 1
        for num in nums[1:]:
            if num != prevNum + 1:
                endNum = prevNum
                ranges.append(createInterval(startNum, endNum))
                startNum = num
                endNum = num
            if currIndex == len(nums) - 1:
                endNum = num
                ranges.append(createInterval(startNum, endNum))
            prevNum = num
            currIndex += 1
        return ranges

        
