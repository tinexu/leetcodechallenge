class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in visited:
                index = visited[complement]
                return [index, i]

            else: 
                visited[nums[i]] = i
