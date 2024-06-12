def findMaximum(list):
    if len(list) == 1:
        return list[0]
    else:
        if list[0] > findMaximum(list[1:]):
            return list[0]
        else:
            return findMaximum(list[1:])
