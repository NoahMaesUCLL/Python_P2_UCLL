# Write your code here
import re 
def thrice_repeated(string):
    return re.fullmatch("(.+)\\1\\1", string)