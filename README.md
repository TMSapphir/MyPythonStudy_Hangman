# MyPythonJourney: Hangman Game 🪝😨



Hello! I'm Tiziano! This is my second repository! I'm currently learning more about Python and now, for training, i've tried to make a small code to replicate the Hangman Game. I've used modules to separate task to train with this tool of python



## 🛠️ Project: The Game


## Arguments: what i'm learning?
In this project I've trained and experimented 

- **modules:** This is my first time that i've used modules in python to separate the work in the code. I have to admit: it seems complicated at first, but it actually made my job much easier because it was easier to read and debug. I definitely think I'll be using modules for everything from now on.
- **ASCI design:** Yeah! I drew all the stages of the hanged man. It was easier than I initially imagined, and thanks to the .append() function, it was also easy to create the list of images.
- **random:** I've tryied to use some random command to randomize the correct word. It's simple because I've not studied yet the randon library.

The Repository has 2 folder



- **Normal Game:** in this folder, i've replicated a normal Handman game. The missing letters are indicated with `_`.

- **Encrypted Game:** in this folder i tried to implement my old XOR encrypter to indicate missing letters.



### 🎉 Normal Game: `Normal`

- In this folder there is the normal game with the `_` indicators

- when the game start, you can insert every character. the code work also with capital letters.

- When you win there is the message: `HAI VINTO!!! LA PAROLA ERA [THE CORRECT WORD]`

- When you loose, you can see the Hangman with the message: `EMOTIONAL DAMAGE! YOU ARE FAILURE!`

- I tried to implement a replay comand, but i've to work to implement it



### 🔐 Encrypted Game: `Encrypted`



- In this folder there is the version of the game where there isn't the normal `_` indicator, but the letter is cripted with a bitwise manipulation with XOR operator. This is the code I used in my first repository and implemented in the game

- For this version I stored the cryptation key in a separated file called `def_keymaster.py`. This is a piece of high italian licterature of the last century.





## 🗑️ Modular Structure


- **The Hangman:** the hangman array is stored in `impiccato_codice.py`.

- **The Correct Word:** the correct words are stored in `codice_parola.py` for the normal game and `codice_gioco_cifrato.py` for the encrypted one. The possibles words are stored in the `a` list and are estracted with a `rd.randint(0, len(word_array)-1)` function that indicate the index of the chosen word. 

- **The Game:** the game motor are stored in `codice_gioco.py` for the normal game and `codice_gioco_cifrato.py` for the encrypted one. 

- **The Encryption Key:** the poem that makes up the encryption key is stored in `def_keymaster.py` 


---

Project created by **TMSapphir** during the Python study program. 😊👋





