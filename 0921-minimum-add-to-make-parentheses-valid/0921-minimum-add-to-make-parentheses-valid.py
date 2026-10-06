class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        insertion = 0 
        balance = 0 
        for ch in s :
            if ch == "(":
                balance += 1 
            elif ch == ")":
                if balance > 0 :
                    balance -= 1 
                else:
                    insertion += 1 
        if balance > 0 :
            insertion += balance 
        return insertion 