# Write your code here
import re 

def ababa(string):
    return re.search("(.+)(.+)\\1\\2\\1", string)