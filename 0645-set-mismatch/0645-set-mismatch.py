class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n*(n+1)//2 
        exp_sq_sum = n*(n+1)*(2*n+1)//6
        actual_sum = 0 
        actual_sq_sum = 0 
        for num in nums:
            actual_sum += num
            actual_sq_sum += num*num
        x = expected_sum - actual_sum 
        y = exp_sq_sum - actual_sq_sum 
        sumAB = y//x
        missing = (x+sumAB)//2
        repeating = missing - x 
        return(repeating, missing)
      