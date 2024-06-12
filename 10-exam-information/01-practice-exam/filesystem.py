# Enter your code here:
class StorageDevice:
    def __init__(self, block_count, block_size):
        self.__available_blocks = set(i for i in range(block_count))
        self.__used_blocks = set()
        self.__block_size = block_size

    @property
    def available_block_count(self):
        return len(self.__available_blocks)
    
    @property
    def used_block_count(self):
        return len(self.__used_blocks)
    
    @property
    def total_block_count(self):
        return self.available_block_count + self.used_block_count
    
    @property
    def block_size(self):
        return self.__block_size
    
    def allocate(self, block_count):
        if len(self.__available_blocks) < block_count:
            raise RuntimeError

        list_available_blocks = list(self.__available_blocks)
        result = []

        for i in range(block_count):
            self.__available_blocks.remove(list_available_blocks[i])
            self.__used_blocks.add(list_available_blocks[i])
            result.append(list_available_blocks[i])

        return result

    def free(self, blocks):
        for block in blocks:
            if block not in self.__used_blocks:
                raise RuntimeError
        
        for block in blocks:
            self.__available_blocks.add(block)
            self.__used_blocks.remove(block)

        list_available_blocks = list(self.__available_blocks)
        list_used_blocks = list(self.__used_blocks)

        self.__available_blocks = set(sorted(list_available_blocks))
        self.__used_blocks = set(sorted(list_used_blocks))

import re
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, storage, name):
        self.__storage = storage
        self.name = name

    @property
    @abstractmethod
    def size_in_blocks(self):
        ...

    @property
    def storage(self):
        return self.__storage

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if not Entity.is_valid_name(new_name): raise RuntimeError

        self.__name = new_name

    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.storage.block_size

    @staticmethod
    def is_valid_name(name):
        if (1 <= len(name) <= 16 and re.fullmatch(r"[a-zA-Z0-9.]*", name)):
            return True
        return False
    
    @abstractmethod
    def clear(self):
        ...

class File(Entity):

    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__size_in_blocks = 0
        self.__occupied = []

    @property
    def size_in_blocks(self):
        return self.__size_in_blocks
    
    def grow(self, block_count):
        new_blocks = self.storage.allocate(block_count)
        self.__occupied.extend(new_blocks)
        self.__size_in_blocks += block_count


    def clear(self):
        self.storage.free(self.__occupied)
        self.__occupied = []
        self.__size_in_blocks = 0

class Directory(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__children = []
    
    @property
    def size_in_blocks(self):
        total_size_in_blocks = 0

        for item in self.__children:
            total_size_in_blocks += item.size_in_blocks

        return total_size_in_blocks

    def add(self, entity):
        self.__children.append(entity)

    def clear(self):
        for item in self.__children:
            item.clear()