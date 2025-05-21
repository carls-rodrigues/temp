class Stack:
    def __init__(self, size):
        self.vector = [None] * size
        self.size = size - 1
        self.base = 0
        self.top = self.base - 1

    def insert(self, data):
        if self.top < self.size:
            self.top += 1
            self.vector[self.top] = data
        else:
            self.size = (self.size + 1) * 2 - 1
            tmp_vector = self.vector
            self.vector = [None] * self.size
            for i in range(len(tmp_vector)):
                self.vector[i] = tmp_vector[i]

    def delete(self):
        if self.top >= self.base:
            self.vector[self.top] = None
            self.top -= 1
        else:
            print("Stack Underflow")

    def inverse(self):
        if self.top < self.base:
            return

        left = self.base
        right = self.top

        while left < right:
            self.vector[left], self.vector[right] = self.vector[right], self.vector[left]
            left += 1
            right -= 1

    def compare_stacks(self, stack):
        if not isinstance(stack, Stack):
            print("Provided object is not a Stack")
            return

        if self.top != stack.top:
            print("The stacks are not equal: different number of elements")
            return

        for i in range(self.top + 1):
            if self.vector[i] != stack.vector[i]:
                print(f"The stacks differ at index {i}: {self.vector[i]} != {stack.vector[i]}")
                return

        print("The stacks are the same")

    def lowest_value(self):
        low = self.vector[0]

        for value in self.vector:
            if value == None:
                break
            
            if value < low:
                low = value
            
        print("The lowest element: " + str(low))

        def __str__(self):
            return str(self.vector[self.base:self.top + 1])

    def top(self):
        if self.top >= self.base:
            return self.vector[self.top]
    
    def destroy(self):
        for i in range(len(self.vector)):
            self.vector[i] = None
            self.base = 0
            self.top = self.base - 1 

if __name__ == "__main__":
    values = [1,5,7,9,11,15,4,13]
    stack = Stack(10)
    stack2 = Stack(10)

    for value in values:
        stack.insert(value)
        stack2.insert(value)

    # print(stack)
    # stack.delete()
    # print(stack)
    stack.inverse()
    # print(stack)
    # stack.delete()
    print(stack.vector)

    stack.compare_stacks(stack2)

    stack.lowest_value()
