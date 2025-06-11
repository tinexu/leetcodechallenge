class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for given word, look through list of all other words.
        # if length of given word and another word is same, then for c in  given word, check that it exists in the other word
        # if at any point it doesnt exist, skip over it, if for loop runs through, add this word to a list to be returned
        # words can be same length but have different frequencies of the same characters... find solution to this
        # best way to check anagrams is sort letters of each word and compare. not good time complexity though :(
        # if a word is an anagram of a given word, the given word is also an anagram of that word. remove added words from the main list
        #maybe i dont need to make this another method... just run while main list is not empty
        # if a given word does not have any other anagrams, the current list of anagrams for current word will only contain current word
        # words are removed from main list as they are added to the current list. current list is added to a result list before being reset to []
        result = []
        def isAnagram(s, t):
            if len(s) != len(t):
                return False
            
            char_counts = [0] * 26

            for i in range(len(s)):
                char_counts[ord((s[i])) - ord('a')] += 1
                char_counts[ord((t[i])) - ord('a')] -= 1
            
            return not any(char_counts)

        while strs:
            current_list = []
            current_word = strs[0]
            current_list.append(current_word)
            strs.remove(current_word)
            length = len(current_word)
            for s in strs:
                if isAnagram(current_word, s):
                    current_list.append(s)
                    strs.remove(s)

            result.append(current_list)
        
        return result



