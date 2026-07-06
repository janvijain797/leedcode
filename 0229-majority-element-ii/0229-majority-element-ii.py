class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        k = len(nums) //3 
        res = [] 
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] +=1 
            else:
                freq[i] = 1 
        for j in freq:
            if freq[j] > k :
                res.append(j)
        return res 