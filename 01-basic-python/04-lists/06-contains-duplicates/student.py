# Write your code here
def contains_duplicates(xs):
    for i in range(len(xs)):
        for k in range (i + 1, len(xs)):
            if xs[i] == xs[k]:
                return True

    return False 