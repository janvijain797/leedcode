class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        total = 1 
        for i in range(n):
            output[i] = total 
            total *= nums[i]
        total = 1 
        for i in range(n-1,-1,-1):
            output[i] *= total 
            total *= nums[i]
        return output 