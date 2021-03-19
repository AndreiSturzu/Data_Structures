from collections import deque


class Stack:
    def __init__(self):
        self.s1 = deque([])
        self.s2 = deque([])

    def push(self, element):
        self.s1.appendleft(element)

    def pop(self):
        if len(self.s1) == 0:
            if len(self.s2) == 0:
                print("stack empty")
            else:
                for i in range(1, len(self.s2)):
                    x = self.s2.pop()
                    self.s1.appendleft(x)
                x = self.s2.pop()
                print(x)
                # print(self.s1, self.s2)
        else:
            for i in range(1, len(self.s1)):
                x = self.s1.pop()
                self.s2.appendleft(x)
            x = self.s1.pop()
            print(x)
            # print(self.s1, self.s2)

    # afiseaza cozile folosite
    def show(self):
        print(self.s1, self.s2)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.show() # afiseaza cozile
s.pop()
s.show()
s.push(4)
s.push(5)
s.show() # afiseaza cozile
s.pop()
s.show() # afiseaza stivele
s.pop()
s.show() # afiseaza stivele



