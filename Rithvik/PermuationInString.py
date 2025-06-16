class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1Count = {}
        s2WindowCount = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for a in alphabet:
            s1Count[a] = 0
            s2WindowCount[a] = 0
        for s in s1:
            s1Count[s] += 1
        left = 0
        right = len(s1) - 1
        for i in range(right + 1):
            s2WindowCount[s2[i]] += 1
        if s1Count == s2WindowCount:
            return True
        while right < len(s2) - 1:
            s2WindowCount[s2[left]] -= 1
            left += 1
            right += 1
            s2WindowCount[s2[right]] += 1
            if s1Count == s2WindowCount:
                return True
        return False
