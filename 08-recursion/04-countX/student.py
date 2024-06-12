def countX(text):
    list_text = list(text)
    count = 0

    for letter in list_text:
        if letter == "x":
            count += 1

    return count

print(countX('XxXx'))