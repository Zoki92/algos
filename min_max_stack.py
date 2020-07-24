"""Write a min max stack class that does:
Pushing and popping values on and off the stack
Peeking the value at the top of the stack
Getting both the minimum and the maximum values in the stack at any given time

All class methods should run in constant time and space

Stack is First in Last Out
"""


class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMax = []

    def pop(self):
        self.minMax.pop()
        print(self.minMax)
        return self.stack.pop()
        

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMax):
            last_min_max = self.minMax[len(self.minMax) - 1]
            newMinMax["min"] = min(last_min_max['min'], number)
            newMinMax["max"] = max(last_min_max['max'], number)
        self.minMax.append(newMinMax)
        self.stack.append(number)
        print(self.stack)
        print(self.minMax)

    
    def getMin(self):
        return self.minMax[len(self.minMax) - 1]['min']

    def getMax(self):
        return self.minMax[len(self.minMax) - 1]['max']

    def peek(self):
        if not self.isEmpty:
            return self.stack[-1]
        
    
    @property
    def isEmpty(self):
        return len(self.stack) == 0


min_max_stack = MinMaxStack()

min_max_stack.push(5)
min_max_stack.push(7)
min_max_stack.push(2)
min_max_stack.pop()
min_max_stack.pop()
