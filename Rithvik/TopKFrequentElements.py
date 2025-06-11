from collections import defaultdict

"""
I think I've done this one before, but this solution is O(len(nums)) rather than
O(klogk) from using a priority queue.A hashmap whose keys are the elements in nums and values are those elements' frequencies
is made with numFreq. Then the key-value pairs are reversed in the form of freqNum, whose keys
are the frequencies and the values are the lists of numbers with those frequencies. While making freqNum, this algorithm
also finds the minimum and maximum frequencies so that it can iterate backwards to make a list with the k most frequent nums.
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        numFreq = defaultdict(int)
        for num in nums:
            numFreq[num] += 1
        minFrequency = 10**6
        maxFrequency = -10**6
        freqNum = defaultdict(list)
        for num, frequency in numFreq.items():
            if frequency < minFrequency:
                minFrequency = frequency
            if frequency > maxFrequency:
                maxFrequency = frequency
            freqNum[frequency].append(num)
        mostFrequentNums = []
        for i in range(maxFrequency, minFrequency - 1, -1):
            if i not in freqNum:
                continue
            if len(mostFrequentNums) == k:
                break
            for num in freqNum[i]:
                mostFrequentNums.append(num)
        return mostFrequentNums




        
                
                
        
