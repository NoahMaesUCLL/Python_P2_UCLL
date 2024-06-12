def merge_dictionaries(d1, d2, merge_function):
    result = dict(d1) #copy dict -- result = d1 <- this references d1
    for k, v in d2.items():
        if k in result:
            result[k] = merge_function(d1[k], d2[k])
        else:
            result[k] = v
        
    return result