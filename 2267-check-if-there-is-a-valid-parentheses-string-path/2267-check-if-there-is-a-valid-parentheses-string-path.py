from collections import deque
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m,n = len(grid),len(grid[0])
        if (m+n-1) % 2 != 0 : 
            return False 
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False 
        queue = deque([(0,0,1)])
        visited = {(0,0,1)}
        while queue : 
            r,c,balance = queue.popleft()
            if(r,c)== (m-1,n-1):
                if balance == 0:
                    return True 
                continue 
            for nr,nc in ((r+1,c),(r,c+1)):
                if nr >= m or nc >= n:
                    continue 
                new_balance = balance + (1 if grid[nr][nc] == '(' else -1)
                if new_balance <0:
                    continue 
                remaining = (m-1-nr) + (n-1-nc)
                if new_balance > remaining :
                    continue 
                state = (nr,nc,new_balance)
                if state not in visited:
                    visited.add(state)
                    queue.append(state)
        return False 

        