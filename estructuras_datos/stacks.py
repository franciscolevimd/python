from collections import deque


class StackDeque:

    def __init__(self):
        self.__items = deque()

    def is_empty(self):
        return len(self.__items) == 0

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        raise IndexError("Empty stack")

    def peak(self):
        if not self.is_empty():
            return self.__items[-1]
        raise IndexError("Empty stack")

    def size(self):
        return len(self.__items)


# Example:
stack_deque = StackDeque()
stack_deque.push(1)
stack_deque.push(2)
print(stack_deque.pop())  # Output: 2
print(stack_deque.peak())  # Output: 1
