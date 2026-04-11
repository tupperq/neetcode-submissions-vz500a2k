class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtracking(openedN, closedN):
            if n == openedN == closedN:
                res.append("".join(stack))
                return

            if openedN < n:
                stack.append('(')
                backtracking(openedN + 1, closedN)
                stack.pop()
            
            if closedN < openedN:
                stack.append(')')
                backtracking(openedN, closedN + 1)
                stack.pop()
            
            return
        
        backtracking(0, 0)
        return res
