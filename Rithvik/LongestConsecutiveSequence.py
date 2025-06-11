from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        So this code DOES run in O(n) time even though it doesn't look that way. For each num in the list, it tries to construct a sequence for which num is the first (and smallest) number.
        It then stores the length of that sequence in the sLens map. This makes it so that if a sequence has been constructed with something like 1, 2, 3, 4, etc. and later in the list is a zero, 
        as soon as it tries to construct a new sequence from zero it will see that a sequence with 1 has already been constructed, and it will use THAT length. 
        """
        added = set() #ensures that if a number is part of an already constructed sequence, it's not added to another sequence (if 3 is in [1,2,3,4] it shouldn't also be added to [2,3,4])
        passedNums = set() #ensures that numbers that are a previous position in a list are not readded to a sequence
        sLens = defaultdict(int) #stores the lengths of the sequences of which the key is the head
        numSet = set(nums) #removes duplicates from nums
        maxLen = 0
        for num in numSet:
            if num in added:
                continue
            currLen = 1
            passedNums.add(num)
            currNum = num
            while currNum + 1 in numSet:
                added.add(currNum + 1)
                if currNum + 1 in passedNums:
                    currLen += sLens[currNum + 1]
                    break
                currLen += 1
                currNum += 1
            sLens[num] = currLen
            if currLen > maxLen:
                maxLen = currLen
        return maxLen
