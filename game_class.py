"""
Wordle solver
"""

GREEN = "🟢"
YELLOW = "🟡"
GREY = "🌑"


class WordleString():
    def __init__(self, string=""):

        self.one = ("", GREY) if not string else (string[0], GREY)
        self.two = ("", GREY) if not string else (string[1], GREY)
        self.three = ("", GREY) if not string else (string[2], GREY)
        self.four = ("", GREY) if not string else (string[3], GREY)
        self.five = ("", GREY) if not string else (string[4], GREY)
        self.bag = list(string.upper())

    def get_letter(self, pos):
        if pos == 1:
            return self.one[0]
        elif pos == 2:
            return self.two[0]
        elif pos == 3:
            return self.three[0]
        elif pos == 4:
            return self.four[0]
        elif pos == 5:
            return self.five[0]

    def get_color(self, pos):
        if pos == 1:
            return self.one[1]
        elif pos == 2:
            return self.two[1]
        elif pos == 3:
            return self.three[1]
        elif pos == 4:
            return self.four[1]
        elif pos == 5:
            return self.five[1]

    def set_color(self, pos, color):
        if pos == 1:
            self.one = (self.one[0], color)
        elif pos == 2:
            self.two = (self.two[0], color)
        elif pos == 3:
            self.three = (self.three[0], color)
        elif pos == 4:
            self.four = (self.four[0], color)
        elif pos == 5:
            self.five = (self.five[0], color)

    def get_bag(self):
        return self.bag

    def get_word(self):
        return "".join(self.bag)


class Guesses():
    def __init__(self, answer):
        self.answer = WordleString(answer)
        self.guess_list = {}
        self.guess_no = 0

    # guess = self.guess_list[self.guess_no]
    def correct(self, guess):

        for i in range(1, 6):
            if self.answer.get_letter(i) == guess.get_letter(i):
                guess.set_color(i, GREEN)

        # YELLOW CASE
        for i in range(1, 6):
            if (self.answer.get_letter(i) != guess.get_letter(i)) \
                    and (guess.get_letter(i) in self.answer.get_bag()):
                guess.set_color(i, YELLOW)

        print(f"Guess is {guess.get_word()}")
        status_string = "".join(guess.get_color(i) for i in range(1,6))
        print(status_string)

        return all(guess.get_color(i) == GREEN for i in range(1, 6))        

    def add_guess(self, guess):
        self.guess_no += 1
        self.guess_list[self.guess_no] = guess

    def get_last_guess(self):
        return self.guess_list[self.guess_no]
