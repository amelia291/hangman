import random
import re
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']


class State:
    def __init__(self):
        self.topic = input('Choose your topic (countries or animals): ')
        self.dict_topics = {'countries': '/Users/amelia/Countries.txt', 'animals': '/Users/amelia/Animals.txt'}
        if self.topic not in self.dict_topics.keys():
            self.topic = input('Wrong topic. Choose your topic (countries or animals): ')
        self.word = open(self.dict_topics[self.topic]).read().splitlines()
        print(self.word)
        self.word_to_guess = random.choice(self.word)
        self.missed_times = 0
        self.missed_letter = []
        self.guessed_letter = []
        self.current_word = re.sub("[0-9a-zA-Z]", "_ ", self.word_to_guess)
        print(self.word_to_guess)
        print(self.current_word)

    def __repr__(self):
        return 'Missed letters: {} \nGuessed letters: {} \n{} \n {}'.format\
            (','.join(self.missed_letter), ','.join(self.guessed_letter), ''.join(self.current_word), HANGMAN_PICS[self.missed_times])

    def guess_a_character(self, char):
        if char in self.word_to_guess:
            if char in self.guessed_letter:
                print(f'You have already guessed that letter. Choose again')
                print(self)
            elif char not in self.guessed_letter:
                self.guessed_letter.append(char)
                for index in range(len(self.word_to_guess)):
                    if self.word_to_guess[index] == char:
                        self.current_word[index] = char
                        print(self)
        if char not in self.word_to_guess:
            self.missed_letter.append(char)
            self.missed_times += 1
            print(self)

    def check_win(self):
        return self.current_word.count('_ ') == 0 and self.missed_times < 6

    def check_lose(self):
        return self.missed_times >= 6

    def reset(self):
        self.missed_times = 0
        self.guessed_letter = []
        self.missed_letter = []
        self.current_word = ['_ ']*len(self.word_to_guess)


state = State()

while not state.check_lose() and not state.check_win():
    guess = input('Guess a letter: ')
    state.guess_a_character(char=guess)

    if state.check_win():
        option = input('Congratulations! You have won! Do you want to play again? (yes or no)')
        if option == 'yes':
            state = State()
        elif option == 'no':
            print(option)

    if state.check_lose():
        print('Correct word:  ' + state.word_to_guess)
        option = input('You have run out of guesses. Do you want to play again? (yes or no)')
        if option == 'yes':
            state = State()
        if option == 'no':
            print(option)




