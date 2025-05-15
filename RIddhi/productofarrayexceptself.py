class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros_count = 0
        for n in nums:
            if n == 0:
                zeros_count += 1
            else:
                product *= n
            
        array = []
        for i in range(len(nums)):
            if (zeros_count >= 2):
                array.append(0)
            elif (zeros_count == 1):
                if (nums[i] == 0):
                    array.append(product)
                else:
                    array.append(0)
            else:
                array.append(product//nums[i])

        return array
