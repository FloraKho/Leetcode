class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.helper_stack = []
        

    def push(self, x: int) -> None:
        
        while len(self.main_stack) > 0:
            self.helper_stack.append(self.main_stack.pop())
        self.main_stack.append(x)
        while len(self.helper_stack) > 0:
            self.main_stack.append(self.helper_stack.pop())
        

    def pop(self) -> int:
        return self.main_stack.pop()

    def peek(self) -> int:
        if len(self.main_stack) > 0:
            return self.main_stack[-1]
        return None

    def empty(self) -> bool:
        if len(self.main_stack) > 0:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


