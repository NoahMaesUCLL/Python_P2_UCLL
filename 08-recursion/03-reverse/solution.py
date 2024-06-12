def reverse_from_left(text):
    if len(text) <= 1:
        return text
    else:
        return reverse_from_left(text[1:]) + text[0]

print(reverse_from_left("hello"))

def reverse_from_right(text):
    if len(text) <= 1:
        return text
    else:
        return text[-1] + reverse_from_right(text[:-1])
    

