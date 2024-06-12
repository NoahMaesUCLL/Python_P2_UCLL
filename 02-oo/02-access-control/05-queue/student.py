class Queue:
    def __init__(self):
        self.__queue = []

    def add(self, item):
        self.__queue.append(item)

    def next(self):
        item = self.__queue[0]
        self.__queue.pop(0)
        return item
    
    def is_empty(self):
        return len(self.__queue) == 0