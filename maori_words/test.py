import os
from os import path

filename = raw_input("enter the file name: ") # type wordsfile.txt
wordinput = raw_input("enter a word: ") # type any word

filepath = os.getcwd() + '/' + filename

maori_dict = {}
def check_if_maoriwords(dict, word):
    result = ''
    for key in dict:
        if key == word:
            result = dict[key]
            break
        else:
            result = 'no such word exists'
    return result

if path.exists(filepath):
    with open(filepath) as file:
        for line in file:
            key_and_value = line.rstrip("\n").split(":")
            maori_dict[key_and_value[0]] = key_and_value[1]
        print check_if_maoriwords(maori_dict, wordinput)
else:
    print 'no such file exists'
