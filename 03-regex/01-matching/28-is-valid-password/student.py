# Write your code here
import re

def is_valid_password(string):
    allowed_regex = [
        r'.{12,}',
        r'[0-9]',
        r'[a-z]',
        r'[A-Z]',
        r'[-+/.*@]'
    ]

    not_allowed_regex = [
        "(.)\\1{2}",
        "(.)(.*\\1){3}"
    ]

    for regex in allowed_regex:
        if not re.search(regex, string):
            return False
    
    for regex in not_allowed_regex:
        if re.search(regex, string):
            return False
        
    return True