# **Hangman Game**
## **7th Mar'23**
## **Overview**
 The Hangman program randomly selects a secret word from a list that we from api.
The Game: Here, a random word (a fruit name) is picked up from list that we get from api and the player gets limited chances to win the game.
When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way,all letters of the word are to be guessed before all the chances are over.
For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five letter word.
## **File used :**
Hangman_game.ipynb
## **How the program works:**
* Creating a list of fruit names the program will pick a word from randomly (from api).
* Display the word but every character is replaced by underscores.
* Ask user to guess character 
* If the user enters right character the program will replace underscore with this character and display the word with underscores and this character all in order
* If enter wrong character it will let the user know that is a wrong character.
* If the user gets all characters right the program will let him know that he won and ask him if he wants to play again.
* If he didnot get the word with available chances he has.the program will let him that he consumed all chances(With displaying the word) and ask him if he wants to play again.
