#20CE082 Harsh Patel
#Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.

class StackBy:
    __dataList = [] #Created empty List

    def push(self, data):
        self.__dataList.append(data) #algo for push

    def pop(self):
        if len(self.__dataList) > 0:  #algo for pop
            return self.__dataList.pop()
        else:
            return "No elements left for popping operation!"

    def get_stackSize(self):
        return len(self.__dataList)

    def printStack(self):
        print(self.__dataList)

    def has_next(self):
        return bool(len(self.__dataList))

    def next(self):
        return self.pop()

    def peek(self):
        if len(self.__dataList) > 0:
            return self.__dataList[-1]
        else:
            return "No Elements are there in stack."

    def printPeek(self):
        print(self.peek())

    def printPop(self):
        print(self.pop())


stack = StackBy()
stack.printStack()
stack.push(1)
stack.printStack()
stack.push("Harsh")
stack.push("82")
print(stack.peek())
stack.printStack()