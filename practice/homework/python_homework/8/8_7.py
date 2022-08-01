class Stack:
    def __init__(self):
        self.data = []

    def empty(self):
        if self.data == []:
            return True
        return False

    def top(self):
        flag = self.empty()
        if flag == True:
            return None
        else:
            return self.data[-1]

    def pop(self):
        flag = self.empty()
        if flag == True:
            return None
        else:
            return self.data.pop(len(self.data)-1)

    def push(self, data):
        self.data.append(data)

    def __repr__(self):
        return f'{self.data}'


    # box = []
    # def __init__(self, data2):
    #     self.data2 = data2

    # @classmethod
    # def empty(cls):
    #     if cls.box:
    #         return True
    #     else:
    #         return False

    # @classmethod
    # def top(cls):
    #     if cls.box:
    #         return cls.box[len(Stack.box)-1]
    #     else:
    #         return None
    
    # @classmethod
    # def pop(cls):
    #     if cls.box:
    #         poppop = cls.box[len(Stack.box)-1]
    #         cls.box.pop()
    #         return poppop
    #     else:
    #         return None

    # def push(self):
    #     Stack.box.append(self.data2)
    #     print(Stack.box)
    #     print(len(Stack.box))

    # def __repr__(self):
    #     return f'{self.data2}'
    


if __name__ == '__main__':
    stack = Stack()

    print(stack.empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.top())
    
    stack.push(4)
    print(stack.pop())
    print(stack.top())


    # print(Stack.empty())
    # a = Stack(1).push()
    # b = Stack(2).push()
    # c = Stack(3).push()
    # print(Stack.pop())
    # print(Stack.top())
