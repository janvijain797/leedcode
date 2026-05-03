class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_arr = sorted(nums)
        for i in range(1, len(sorted_arr)):
            if sorted_arr[i-1] == sorted_arr[i]:
                return sorted_arr[i]
        return -1 