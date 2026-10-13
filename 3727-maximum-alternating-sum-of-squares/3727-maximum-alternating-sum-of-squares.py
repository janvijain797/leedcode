class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = []

        for x in nums:
            arr.append(x * x)

        arr.sort()

        n = len(arr)
        score = 0

        for i in range(n // 2):
            score -= arr[i]

        for i in range(n // 2, n):
            score += arr[i]
        return score
