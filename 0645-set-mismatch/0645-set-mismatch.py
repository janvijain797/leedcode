class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [] 
        sorted_arr = sorted(nums)
        for i in range(1,n):
            if sorted_arr [i-1] == sorted_arr[i]:
                duplicate = sorted_arr[i]
                break  
        expacted_sum = n*(n+1)//2
        actual_sum = sum(nums)
        missing_num = expacted_sum - (actual_sum -duplicate)
        return [duplicate,missing_num ]
