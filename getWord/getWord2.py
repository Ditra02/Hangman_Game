# This program will get the word for hangman game
# the flow of this program
# 1. opening the github repo url
# 2. read and decode words in the page
# 3. opening txt file
# 4. writing words which have read
# 5. read and keep words in list data type

# module that helping to open the url
import urllib.request as request
import os


os.system('cls')
os.system('color b')

# the url of raw of github repo
url = request.urlopen(
    'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt')

# opening that raw webpage
with url as f:

    # read and encode the webpage with utf-8 encoding
    f = f.read().decode('utf-8')

    # open txt file to store the data
    with open('test.txt', 'w') as txt:

        # writing the data from webpage to txt file
        txt.write(f)

        # opening the txt file for reading the data
        with open('test.txt', 'r') as txt:
            # read the data line by line (it become a list)
            txt = txt.readlines()

            # removing the '\n' character from each word in txt list
            word = [i.rstrip('\n') for i in txt]



