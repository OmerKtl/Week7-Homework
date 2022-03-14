""""
Write a program that detects the ID number hidden in a text. We know that the format of the ID number is 2 letters, 1 digit,
2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6

Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678

Output : VZ4PF94B6
"""
import re

def id_detect(number):
    patern=r"\w{2}\d\w{2}\d{2}\w\d"
    hid_id=re.search(patern,number)
    return hid_id.group()
    

number=input("Enter a text with the ID number hidden in it :")#SDFEG234335AA4ZA11B1RRHUKYDD67GJ66

print("The Hidden ID :",id_detect(number))