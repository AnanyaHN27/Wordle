"""
Wordle solver
"""

GREEN = "🟢"
YELLOW = "🟡"
GREY = "🌑"


class WordleString():
    def __init__(self, string=""):
        self.letters = [(("", GREY) if not string else (string[i], GREY)) for i in range(0, 5)]
        self.bag = list(string.upper())

    def get_letter(self, pos):
        return self.letters[pos-1][0]

    def get_color(self, pos):
        return self.letters[pos-1][1]

    def set_color(self, pos, color):
        self.letters[pos-1] = (self.letters[pos-1][0], color)

    def get_bag(self):
        return self.bag

    def get_word(self):
        return " ".join(self.bag)


class Guesses():
    def __init__(self, answer):
        self.answer = WordleString(answer)
        self.guess_list = {}
        self.guess_no = 0

    def correct(self, guess):

        for i in range(1, 6):
            if self.answer.get_letter(i) == guess.get_letter(i):
                guess.set_color(i, GREEN)

        # YELLOW CASE
        for i in range(1, 6):
            if (self.answer.get_letter(i) != guess.get_letter(i)) \
                    and (guess.get_letter(i) in self.answer.get_bag()):
                guess.set_color(i, YELLOW)

        print(guess.get_word())
        status_string = "".join(guess.get_color(i) for i in range(1,6))
        print(status_string)

        return all(guess.get_color(i) == GREEN for i in range(1, 6))        

    def add_guess(self, guess):
        self.guess_no += 1
        self.guess_list[self.guess_no] = guess

    def get_last_guess(self):
        return self.guess_list[self.guess_no]
