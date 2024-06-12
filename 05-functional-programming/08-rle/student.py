def rle_encode(data):    
    letters_list = []
    letter_count = 0

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            letter_count += 1
        else:
            letters_list.append((f'{data[i - 1]}', letter_count + 1))
            letter_count = 0

    letters_list.append((f'{data[-1]}', letter_count + 1))
    
    return letters_list

def rle_decode(data):
    return_strring = ""

    for letter, count in data:
        for _ in range(count):
            return_strring += letter

    return return_strring