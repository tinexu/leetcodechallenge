class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charMap = {}
        seenChars = set()

        for i in range(len(s)):
            if s[i] not in charMap:
                if t[i] in seenChars:
                    return False
                charMap[s[i]] = t[i]
                seenChars.add(t[i])
            else:
                if charMap[s[i]] != t[i]:
                    return False
        return True
        
