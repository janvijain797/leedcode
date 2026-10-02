class Solution:
    def solve(self,index,total,bracket,result):
        if index >= len(bracket):
            if total == 0:
                result.append("".join(bracket))
            return 
        elif total > len(bracket)//2:
            return 
        if total <0 :
            return 
        bracket[index] = "("
        sum = total + 1 
        self.solve(index+1,sum, bracket,result)
        bracket[index] = ")"
        sum = total-1 
        self.solve(index+1,sum, bracket,result)

    def generateParenthesis(self, n: int) -> list[str]:
        bracket = [""]*(2*n)
        result =  [] 
        self.solve(0,0,bracket,result)
        return result 
        