# Write your code here
def double_dict_values(dictionary):
    result = {}
    for k, v in dictionary.items():
        result[k] = v * 2

    return result