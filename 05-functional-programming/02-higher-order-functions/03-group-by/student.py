def group_by(xs, key_function):
    result_dict = {}
    for x in xs:
        key = key_function(x)
        if key not in result_dict:
            result_dict[key] = []
        result_dict[key].append(x)

    return result_dict