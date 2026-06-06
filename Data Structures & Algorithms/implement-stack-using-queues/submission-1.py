from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque([])
        self.size = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1
        for i in range(self.size-1):
            y = self.queue.popleft()
            self.queue.append(y)

    def pop(self) -> int:
        y = self.queue.popleft()
        self.size -= 1
        return y
        

    def top(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return self.size == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()