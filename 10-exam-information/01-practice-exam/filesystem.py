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

        for i in range(block_count):
            self.__available_blocks.remove(list_available_blocks[i])
            self.__used_blocks.add(list_available_blocks[i])

    def free(self, blocks):
        for block in blocks:
            if block not in self.__used_blocks:
                raise RuntimeError
        
        for block in blocks:
            self.__used_blocks.remove(block)
            self.__available_blocks.add(block)

        list_available_blocks = list(self.__available_blocks)
        list_used_blocks = list(self.__used_blocks)

        self.__available_blocks = set(sorted(list_available_blocks))
        self.__used_blocks = set(sorted(list_used_blocks))


import re
class Entity:
    def __init__(self, storage, name):
        self.__storage = storage
        self.name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name_text):
        if not Entity.is_valid_name(name_text): raise RuntimeError

        self.name = name_text

    @staticmethod
    def is_valid_name(name):
        if (1 < len(name) < 16 and re.fullmatch("[a-zA-Z0-9\.]*", name)):
            return True
        return False