def sum_numbers(number):
    number = abs(number)
    
    if number < 10:
        return number
    
    return (number % 10) + sum_numbers(number // 10)


print(sum_numbers(123))
    