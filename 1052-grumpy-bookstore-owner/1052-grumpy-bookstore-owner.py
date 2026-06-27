class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        satisfied_customers = 0 
        for i in range(n):
            if grumpy[i] == 0 :
                satisfied_customers += customers[i] 
        max_satisfied = 0 
        additional_satisfied = 0 
        for i in range(minutes):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
        max_satisfied = additional_satisfied
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if grumpy[i-minutes]:
                additional_satisfied -= customers[i-minutes]
            max_satisfied = max(max_satisfied, additional_satisfied)
        return satisfied_customers + max_satisfied 
        