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
    list_available_blocks = list(available_blocks)
    list_used_blocks = list(used_blocks)

    available_blocks = set(sorted(list_available_blocks))
    used_blocks = set(sorted(list_used_blocks))
    
    for block in blocks:
        if block not in used_blocks:
            raise RuntimeError
        
    for block in blocks:
        used_blocks.remove(block)
        available_blocks.add(block)

import re

def is_valid_name(name):
    if (1 < len(name) < 16 and re.fullmatch("[a-zA-Z0-9\.]*", name)):
        return True
    
    return False

print(is_valid_name("testDAS12.3dsadasff"))

