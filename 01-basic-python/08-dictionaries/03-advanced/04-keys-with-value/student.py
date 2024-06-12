# Write your code here
def keys_with_value(dictionary, value):
    result = []
    for k, v in dictionary.items():
        if v == value:
            result.append(k)

    return result