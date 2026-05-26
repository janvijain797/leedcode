class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0]+nums[1]+nums[2]
        for i in range(0,n):
            left = i+1
            right = n-1
            while left<right:
                current_sum = nums[i]+ nums[left]+ nums[right]
                if abs(current_sum - target)< abs(closest_sum- target):
                    closest_sum = current_sum 
                if current_sum<target :
                    left = left+1 
                elif current_sum> target:
                    right = right -1 
                else:
                    return current_sum 
        return closest_sum 
