# Write your code here
def merge_dicts(dictionary_one, dictionary_two):
    merged_dict = dict(dictionary_one)
    for k, v in dictionary_two.items():
        merged_dict[k] = v

    return merged_dict