# Write your code here
def median(ns):
    ns = sorted(ns)
    middle_index = len(ns) // 2 

    if(len(ns) % 2 == 1):
        return ns[middle_index]
    
    return ((ns[middle_index] + ns[middle_index - 1]) / 2)