class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        ans = [] 
        for query in queries :
            index = self.binary_search(nums,query)
            ans.append(index)
        return ans 
    def binary_search(self, nums,target):
        left, right = 0 ,len(nums)-1 
        while left<= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid+1
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        return left         