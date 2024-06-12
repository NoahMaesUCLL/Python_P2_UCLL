available_blocks = set(i for i in range(10))
used_blocks = set()
   
def allocate(block_count):
    if len(available_blocks) < block_count:
        raise RuntimeError
    
    list_available_blocks = list(available_blocks)
    for i in range(block_count):
        available_blocks.remove(list_available_blocks[i])
        used_blocks.add(list_available_blocks[i])

def free(blocks):
    for block in blocks:
        if block not in used_blocks:
            raise RuntimeError
        
    for block in blocks:
        used_blocks.remove(block)
        available_blocks.add(block)

    available_blocks = set(sorted(available_blocks))
    used_blocks = set(sorted(used_blocks))

import re

def is_valid_name(name):
    if (1 < len(name) < 16 and re.fullmatch("[a-zA-Z0-9\.]*", name)):
        return True
    
    return False

test_set = set()
test_set.add(1)
test_set.add(0)
test_set.add(4)
test_set.add(5)
test_set.add(2)
test_set.add(3)



print(sorted(test_set))
