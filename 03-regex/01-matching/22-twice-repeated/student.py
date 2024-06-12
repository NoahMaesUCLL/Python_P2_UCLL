# Write your code here
import re

def twice_repeated(string):
    return re.fullmatch("(.+)\\1", string)