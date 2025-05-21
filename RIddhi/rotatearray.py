class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l = len(nums)
        sub_front = nums[l - k: l]
        sub_end = nums[0:l - k]
        index = 0
        for i in range(len(sub_front)):
            nums[index] = sub_front[index]
            index += 1

        for j in range(len(sub_end)):
            nums[index] = sub_end[j]
            index += 1

        
