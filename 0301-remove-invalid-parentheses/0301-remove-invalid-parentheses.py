class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = 0 
        right = 0 
        for i in range(len(s)):
            if s[i] =="(":
                left += 1 
            elif s[i] == ")":
                if left > 0 :
                    left -= 1
                else :
                    right += 1 
        result = set()
        def dfs(index,left_rem,right_rem,balance,current):
            if balance < 0:
                return
            if index == len(s):
                if left_rem == 0 and right_rem == 0 and balance == 0:
                    result.add(current)
                return
            ch = s[index]
            if ch == "(":
                if left_rem > 0:
                    dfs(
                        index + 1,
                        left_rem - 1,
                        right_rem,
                        balance,
                        current
                    )

                dfs(
                    index + 1,
                    left_rem,
                    right_rem,
                    balance + 1,
                    current + ch
                )

            elif ch == ")":
                if right_rem > 0:
                    dfs(
                        index + 1,
                        left_rem,
                        right_rem - 1,
                        balance,
                        current
                    )

                if balance > 0:
                    dfs(
                        index + 1,
                        left_rem,
                        right_rem,
                        balance - 1,
                        current + ch
                    )

            else:

                dfs(
                    index + 1,
                    left_rem,
                    right_rem,
                    balance,
                    current + ch
                )

        dfs(0, left, right, 0, "")

        return list(result)
        