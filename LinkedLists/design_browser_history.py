"""
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

"""

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        home_page_node = Node(homepage)
        self.current_page = home_page_node
        self.head = home_page_node
        self.tail = home_page_node

    def visit(self, url: str) -> None:
        new_node = Node(url, self.current_page, None)
        self.current_page.next = new_node
        self.tail = new_node
        self.current_page = new_node

    def back(self, steps: int) -> str:

        for step in range(steps):

            if self.current_page == self.head:
                break
            else:
                self.current_page = self.current_page.prev

        return self.current_page.value

    def forward(self, steps: int) -> str:

        for step in range(steps):
            if self.current_page == self.tail:
                break
            else:
                self.current_page = self.current_page.next
        return self.current_page.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
