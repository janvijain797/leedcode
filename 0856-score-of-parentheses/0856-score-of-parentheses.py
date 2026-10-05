class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0 
        depth = 0  
        for ch in range(len(s)) :
            if s[ch] == "(":
                depth += 1 
            else:
                depth -= 1
                if s[ch-1] == "(":
                    score += 2**depth
        return score