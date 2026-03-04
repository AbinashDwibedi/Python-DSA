class MinStack:
    st = list()
    minVal = float("inf")
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.st.append(val)
            self.minVal = val
        else:
            if val >= self.minVal:
                self.st.append(val)
            else:
                tmp = (2*val) - self.minVal
                self.st.append(tmp)
                self.minVal = val

    def pop(self) -> None:
        if self.minVal > self.st[-1]:
            tmp = (2*self.minVal) - self.st[-1]
            self.st.pop()
            self.minVal = tmp
        else:
            self.st.pop()

    def top(self) -> int:
        if self.minVal > self.st[-1]:
            return self.minVal
        return self.st[-1]

    def getMin(self) -> int:
        return self.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()