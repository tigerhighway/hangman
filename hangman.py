HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




class Hangman:

    def __init__(self):
        self.guess = []
        self.index = 0

    def printhangman(self, word, guesses):
        self.index = 0
        for g in guesses:
            if g not in word:
                self.index += 1
        print(HANGMANPICS[self.index])

    def printhiddenword(self, word, guess):
        underscore = ""
        for c in word:
            if c not in guess:
                underscore += "_ "
            else:
                underscore += c
        if underscore == word:
            print("You win.")
        elif self.index == 6:
            print("You lost")
        else:
            print(underscore)
        
    def selectsecret(self):
        return 'gitesh'
        
    def play(self):
        word = self.selectsecret()
        while True:
            self.printhangman(word, self.guess)
            self.printhiddenword(word, self.guess)
            print("type 'q' to quit the game")
            inp = input()
            if inp == 'q':
                break
            else:
                self.guess.append(inp)
            if self.index == 6:
                break
