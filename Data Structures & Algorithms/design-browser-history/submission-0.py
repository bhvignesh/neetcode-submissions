class Node:
    def __init__(self, page=0, next=None, prev = None):
        self.page = page
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.size = 1
        self.curr = self.head

    def visit(self, url: str) -> None:
        new_page = Node(url, None, self.curr)
        self.curr.next = new_page
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev != None:
                self.curr = self.curr.prev
        return self.curr.page

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next!=None:
                self.curr = self.curr.next
        return self.curr.page
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)