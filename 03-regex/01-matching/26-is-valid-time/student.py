# Write your code here
import re

def is_valid_time(string):
    return re.fullmatch("([01][0-9]|[02][0-3]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]{3})?", string)

print(is_valid_time("23:59:59"))
