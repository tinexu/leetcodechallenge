from collections import defaultdict
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        stringLocs = defaultdict(list)
        for i in range(len(list1)):
            striangLocs[list1[i]].append(i)
        for i in range(len(list2)):
            stringLocs[list2[i]].append(i)

        minSum = 3000
        for pair in stringLocs.values():
            if len(pair) != 2:
                continue
            if pair[0] + pair[1] < minSum:
                minSum = pair[0] + pair[1]
        commonStrings = []
        for item in stringLocs.items():
            pair = item[1]
            if len(pair) != 2:
                continue
            if pair[0] + pair[1] == minSum:
                commonStrings.append(item[0])
        return commonStrings
        
