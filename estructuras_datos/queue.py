from collections import deque


class Queue:

    def __init__(self):
        self.__items = deque()

    def is_empty(self):
        return len(self.__items) == 0

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.__items.popleft()
        raise IndexError("Empty queue")

    def front(self):
        if not self.is_empty():
            return self.__items[0]
        raise IndexError("Empty queue")

    def size(self):
        return len(self.__items)


# Example:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
print(queue.front())    # Output: 2
