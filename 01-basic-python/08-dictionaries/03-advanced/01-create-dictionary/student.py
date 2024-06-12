# Write your code here
def create_dictionary(keys, values):
    result = dict()
    for k, v in zip(keys, values):
        result[k] = v
    
    return result

def create_dictionary(keys, values):
    return dict(zip(keys, values))