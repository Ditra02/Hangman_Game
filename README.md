# Hangman_Game

<div align="center">
  <br>
  <img src="https://i.gyazo.com/81ca3e17a698bd712d0766d50ca0cef7.png" alt="Hangman Logo" width="500">
</div>

<br>

When I made this game, I divide the process into 3 part below:
1. Get the word that will be guessed by player <br>
   I get the words from github repository simply by put the link of the txt file inside `getWords1.py` and it will be opened by urllib. Finally, the words saved as a list. You can see the implementation in [getWords](https://github.com/Ditra02/Hangman_game/tree/main/getWord) file.

2. The Flow of the game correspond to the rules <br>
   I made flowchart to map all condition where the player got wrong or true while guessed a letter and win or lose at the end of the game. You can see the flowchart [here](https://github.com/Ditra02/Hangman_game/blob/main/hangman_flowchart.drawio.png) or you can see the detail of the game [here](https://en.wikipedia.org/wiki/Hangman_(game)).
   
3. Chance visualization <br>
   I also used [visualization](https://raw.githubusercontent.com/kying18/hangman/master/hangman_visual.py) which exists in github repository. Same as before, I used the urllib module to get the file and saved it as a `visualLives.py`.
   
<hr>
References: <br>

* [urllib3](https://pypi.org/project/urllib3)
