class CircularBuffer:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__list = []

    def __len__(self):
        return len(self.__list)
    
    def __getitem__(self, index):
        return self.__list[index]
    
    def add(self, item):
        if(len(self.__list) == self.__max_size):
            self.__list.pop(0)
        self.__list.append(item)