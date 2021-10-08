STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"
GUESSES = 9


class Hangman(object):
    def __init__(self, word):
      self.remaining_guesses = GUESSES
      self.status = STATUS_ONGOING
      self.__word = word
      self.__guesses = set()

    def guess(self, char):
      if self.status != STATUS_ONGOING:
        raise ValueError("Game over!")
      if self.__word.find(char) != -1 and (char not in self.__guesses):
        self.__guesses.add(char)
      else:
        self.remaining_guesses -= 1
      
      if self.__guesses == set(self.__word):
        self.status = STATUS_WIN


    def get_masked_word(self):
      return "".join('_' if c not in self.__guesses else c for c in self.__word)

    def get_status(self):
      if self.remaining_guesses < 0:
        self.status = STATUS_LOSE
      return self.status