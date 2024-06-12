class InclusiveRange:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def __iter__(self):
        return InclusiveRangeIterator(self.__start, self.__end)
    
class InclusiveRangeIterator:
    def __init__(self, start, end):
        self.__index = start
        self.__end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index > self.__end:
            raise StopIteration()
        else:
            result = self.__index
            self.__index += 1
            return result

    