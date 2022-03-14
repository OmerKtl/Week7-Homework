""""
Write a program that list according to email addresses without email domains in a text.

Example:

Input:

The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. 
Then New Yorker article on wind farms...

Output :

franky

sinatra123
"""
import re
sentence="The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."
patern=r"(\w+)(@)"
for matching in re.finditer(patern,sentence):
    print(matching.groups()[0])