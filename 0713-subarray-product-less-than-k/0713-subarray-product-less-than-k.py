class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return k
        cnt = 0 
        prod = 1 
        i = 0 
        for j in range (len(nums)):
            prod *= nums[j]
            while i<=j and prod >=k :
                prod /= nums[i]
                i+=1 
            cnt += j-i+1
        return cnt 