import random
import requests
import json
import streamlit as st
def inputs () :
    """
    Choose which fruit the game will be about
    Return :
    (str) word - fruit name from the list
    """
    # fruit list from api to get all fruit names
    url='https://fruityvice.com/api/fruit/all'
    result=requests.get(url)
    result=result.json()
    lst=[]
    for fruit in result :
        lst.append(fruit['name'].strip().lower())
    # choose word randomly among the fruit list
    word=random.choice(lst)
    return word

def underscore_gen(word):
    """
    create a list that have each character of the fruit name replaced by underscores except spaces 
    Returns :
    (list) lst1 - characters of fruit name replaced by  except spaces
    """
    lst1=[]
    for i in range (0,len(word),1) :
        if word[i]== " " :
            lst1.append(" ")
        else :
            lst1.append("_")
    # Give the user the Name of fruit and each character of the fruit is replaced by underscore
    s=" ".join(lst1)
    print(s)
    return lst1

HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word=inputs()
lst1=underscore_gen(word)
if 'curr_word' not in st.session_state:
    st.session_state.curr_word = word
    st.session_state.guess_list = lst1
    st.session_state.man = 0
    st.session_state.guessed_letters = []
    st.session_state.game_over = False
    st.session_state.message = ""  # Store only the latest message
st.title('Hangman Game')
st.write('Guess the fruit name!')

# Display the current state of the word
st.write(f"Word to guess: {' '.join(st.session_state.guess_list)}")

# Display the current hangman picture using st.code for better formatting
st.code(HANGMANPICS[st.session_state.man])

# Use a form to handle both the submit button and Enter key for guessing
with st.form(key='guess_form'):
    guess = st.text_input("Guess a letter", max_chars=1)
    submit_button = st.form_submit_button("Submit Guess")

if submit_button and not st.session_state.game_over:
    if guess and guess.isalpha() and len(guess) == 1:
        guess = guess.lower()
        if guess in st.session_state.guessed_letters:
            st.session_state.message = f"You already guessed '{guess}'. Try a different letter."
        else:
            st.session_state.guessed_letters.append(guess)
            if guess in st.session_state.curr_word:
                for i, letter in enumerate(st.session_state.curr_word):
                    if letter == guess:
                        st.session_state.guess_list[i] = letter
                st.session_state.message = f"Good guess! {guess} is in the word."
            else:
                st.session_state.man += 1
                st.session_state.message = f"Wrong guess! {guess} is not in the word."
    
    # Force a re-render to immediately show updated state
    st.rerun()
if "_" not in st.session_state.guess_list:
    st.session_state.message = f"Congratulations! You've guessed the word: {''.join(st.session_state.guess_list)}"
    st.session_state.game_over = True
elif st.session_state.man >= len(HANGMANPICS) - 1:
    st.session_state.message = f"You've run out of lives! The word was: {st.session_state.curr_word}"
    st.session_state.game_over = True

# Display only the latest message
if st.session_state.message:
    if "Congratulations" in st.session_state.message or "You've run out of lives" in st.session_state.message:
        st.success(st.session_state.message)
    elif "Good guess" in st.session_state.message:  # Show "Good guess" message in green
        st.success(st.session_state.message)
    elif "Wrong guess" in st.session_state.message:  # Show wrong guess in red
        st.error(st.session_state.message)
    else:
        st.warning(st.session_state.message)

# Reset the game
if st.session_state.game_over:
    if st.button("Play Again"):
        # Reset the session state for a new game
        st.session_state.curr_word = word
        st.session_state.guess_list = lst1
        st.session_state.man = 0
        st.session_state.guessed_letters = []
        st.session_state.message = ""  # Reset message
        st.session_state.game_over = False
        st.rerun()
