class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        r = 0 
        total = 0 
        Ans = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                Ans = min(Ans, r-l+1)
                total -= nums[l]
                l+=1
        return 0 if Ans == float("inf") else Ans
        