class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        charsT = {}
        charsS = {}
        letters = "abcdefghijklmnopqrstuvwxyz"
        for character in letters:
            charsS[character] = 0
            charsT[character] = 0
        for i in range(len(s)):
            charsS[s[i]] += 1
            charsT[t[i]] += 1
        for character in letters:
            if charsS[character] != charsT[character]:
                return False
        return True
