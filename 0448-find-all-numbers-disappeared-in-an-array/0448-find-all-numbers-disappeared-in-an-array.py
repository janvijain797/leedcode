class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        all_nums= set(range(1,n+1))
        missing_numbers = all_nums - num_set
        return list(missing_numbers)
        