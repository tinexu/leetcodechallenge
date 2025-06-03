class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        modIntervals = []
        inserted = False
        for interval in intervals:
            if interval[0] > newInterval[0] and inserted == False:
                modIntervals.append(newInterval)
                inserted = True
            modIntervals.append(interval)
        if not inserted:
            modIntervals.append(newInterval)
        mergedIntervals = [modIntervals[0]]
        if len(modIntervals) == 1:
            return mergedIntervals
        currIndex = 0
        for interval in modIntervals[1:]:
            if interval[0] <= mergedIntervals[currIndex][1]:
                mergedIntervals[currIndex][1] = max(interval[1], mergedIntervals[currIndex][1])
            else:
                mergedIntervals.append(interval)
                currIndex += 1
        return mergedIntervals
        
