# Write your code here
def remove_duplicates(xs):
    found = set()
    result = []

    for i in xs:
        if i not in found:
            found.add(i)
            result.append(i)

    return result