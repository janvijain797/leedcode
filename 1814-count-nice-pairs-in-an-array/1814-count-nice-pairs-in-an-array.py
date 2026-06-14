class Solution:
    def rev(self, num):
        return int(str(num)[:: -1])
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7 
        count = {}
        nice_pairs = 0 
        for num in nums:
            diff = num - self.rev(num)
            print(diff)
            if diff in count:
                nice_pairs += count[diff]
            count[diff] = count.get(diff,0)+1
        return nice_pairs % MOD