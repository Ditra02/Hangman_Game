# This program is getting the words from github repo and keep it in a list data type
# The flow of this program
# 1. opening the github repo url
# 2. read and decode words
# 3. keep the words in list data type

# importing module
import os
import urllib.request as request        # module to help open the url

# clear the terminal and change the color to blue
os.system('cls')
os.system('color b')

# open the url to get the words from raw github repository
url = request.urlopen(
    'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt')

# opening the url
with url as f:
    # read the url and decode the url
    f = f.read().decode('utf-8')

    # since we read a whole from url so it become a string when we keep it in f
    # in order to fix it we have to split this string with the splitter '\n'
    # because in the end of each word has '\n'
    word = f.split('\n')
# print(word)
