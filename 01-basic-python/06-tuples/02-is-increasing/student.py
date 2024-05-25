# Write your code here
def is_increasing(ns):
    combined_list = list(zip(ns, ns[1:]))
    for i in combined_list:
        if (i[0] > i[1]):
            return False
    
    return True