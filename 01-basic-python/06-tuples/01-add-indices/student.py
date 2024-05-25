# Write your code here
def add_indices(xs):
    number_list = []
    for i in range(len(xs)):
        number_list.append(i)
    
    return list(zip(number_list, xs))

def add_indices(xs):
    indices = range(len(xs))
    return list(zip(indices, xs))

def add_indices(xs):
    return list(enumerate(xs))