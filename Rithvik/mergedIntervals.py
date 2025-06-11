from collections import defaultdict
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]

        Because the range of values is about the same size as the maximum length of the intervals list, I determined that counting sort would be faster than using sorted(). 
        Anyway after sorting it, I used the fact that if you have two intervals [a,b] and [c,d] and c >= a, b >= a, and d >= c, they're overlapping if and only if 
		    c <= b and if they are overlapping, [a,b] union [c,d] can be rerwritten as [a, max(b, d)] and from then on it's fairly self-explanatory I think.
        """
        startNums = defaultdict(list)
        maxStart = -10**4 - 1
        minStart = 10**4 + 1
        for interval in intervals:
            firstNum = interval[0]
            if firstNum > maxStart:
                maxStart = firstNum
            if firstNum < minStart:
                minStart = firstNum
            startNums[firstNum].append(interval)
        sortedIntervals = []
        for i in range(minStart, maxStart + 1):
            for interval in startNums[i]:
                sortedIntervals.append(interval)
        mergedIntervals = [sortedIntervals[0]]
        if len(sortedIntervals) == 1:
            return mergedIntervals
        currIndex = 0
        for interval in sortedIntervals[1:]:
            if interval[0] <= mergedIntervals[currIndex][1]:
                mergedIntervals[currIndex][1] = max(mergedIntervals[currIndex][1], interval[1])
            else:
                mergedIntervals.append(interval)
                currIndex += 1
        return mergedIntervals            

    



        
