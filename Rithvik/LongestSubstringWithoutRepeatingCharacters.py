class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        charLocs = {}
        smallestIndex = 0
        for i in range(len(s)):
            if s[i] in charLocs:
                recentLoc = charLocs[s[i]]
                for j in range(smallestIndex, recentLoc + 1):
                    del charLocs[s[j]]
                smallestIndex = recentLoc + 1
            charLocs[s[i]] = i
            maxLen = max(maxLen, len(charLocs))
        return maxLen
