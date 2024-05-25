# Write your code here
def lookup(dictionary, key):
    for k, v in dictionary.items():
        if k == key:
            return v

def lookup(dictionary, key):
    return dictionary[key]