class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seenNums = set()
        while n != 1:
            seenNums.add(n)
            newNum = 0
            for digit in str(n):
                digitInt = int(digit)
                newNum += (digitInt * digitInt)
            n = newNum
            if n in seenNums:
                return False
        return True
