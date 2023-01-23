# this program helps get lives visualization that match with step to death
# 1. opening the github repo url
# 2. read and decode contents in the page
# 3. open .py file
# 4. writing contents that have read in .py file

# importing the module that will help open the url
import urllib.request as request

# open the url. url of raw github repo
url = request.urlopen(
    r'https://raw.githubusercontent.com/kying18/hangman/master/hangman_visual.py')

# read and decode contents in the url
page = url.read().decode('utf-8')

# make file visualLives.py, open, and write
with open(r'D:\0.PYTHON\100 days code\recite\day 7 hangman\hangman by me\getVisualLives\visualLives.py', 'w') as f:

    # writing all content from the page
    f.write(page)
