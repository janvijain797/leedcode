class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums , target):
            n = len(nums)
            low = 0 
            high = n-1 
            res = -1 
            while low <= high :
                mid= (low + high)//2 
                if nums[mid] > target:
                    high = mid -1 
                elif nums[mid] < target :
                    low = mid +1 
                else :
                    res = mid 
                    high = mid-1 
            return res 
        def last(nums , target):
            n = len(nums)
            low = 0 
            high = n-1 
            res = -1 
            while low <= high :
                mid= (low + high)//2 
                if nums[mid] > target:
                    high = mid -1 
                elif nums[mid] < target :
                    low = mid +1 
                else :
                    res = mid 
                    low = mid +1 
            return res 
        return [first(nums , target),last(nums ,target)]       
