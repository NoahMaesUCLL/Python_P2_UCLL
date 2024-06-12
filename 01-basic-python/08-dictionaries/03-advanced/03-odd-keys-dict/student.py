# Write your code here
def odd_keys_dict(dictionary):
    result = {}
    for k, v in dictionary.items():
        if k % 2 == 1:
            result[k] = v

    return result