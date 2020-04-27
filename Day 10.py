class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = inf
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.min_val:
            self.min_val = x        

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_val:
            self.get_new_min_val()
        
    def get_new_min_val(self):
        curr_min = inf
        for val in self.stack:
            if val < curr_min:
                curr_min = val
        self.min_val = curr_min        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
