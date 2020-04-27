class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.type(S) == self.type(T)
    
    def type(self, s) -> str:
        A = ""
        for x in s:
            if x is "#":
                A = A[:len(A)-1]
            else:
                A += x
        return A
