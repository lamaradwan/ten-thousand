from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker

"""
# IMPORTANT: 

1- before you start work, get the updated version of the project by applying this command (git pull origin main)

2- When ever you are adding new feature to this project,always create a branch and make the branch name meaningful,
don't name it saleh,Sara ,etc..

3- test the code before you push it to Github by applying this command pytest -v , to make sure that your work doesn't
effect the previous work

4- if all the tests passes ,you can push your branch and merge it 

"""


class Game:

    def __init__(self):
        self.round_counter = 1
        self.dice_remaining = 6
        self.user_answer = ""
        self.banker = Banker()

    def starting_round(self, roller):
        """
        | This Function Will Be Called In Each New Roll, A Tuple With Random Numbers Between 1 And 6 Will Be Passed To
        | This Function,The Tuple Length Depending On The Remaining Dices
        | :param roller:
        | :return: No output
        """

        if len(roller) == 6:
            print(f'Starting round {self.round_counter}')

        self.roll_dices(roller)
        print('Enter dice to keep, or (q)uit:')
        self.user_answer = input("> ")

    def bank(self):
        """
        This Function Will Called It Each Roll To Calculate The Total Score And Check If The Player Wants To Bank The
        Shelved Points Or Not
        :return: No Output
        """

        self.user_answer = (tuple(map(int, self.user_answer)))
        self.dice_remaining -= len(self.user_answer)
        self.banker.shelved += GameLogic.calculate_score(self.user_answer)
        self.show_shelf_points_and_options()
        self.user_answer = input("> ")

        if self.user_answer == "b":
            self.dice_remaining = 6
            self.banked_and_total_points_msg()
            self.round_counter += 1

    def play(self, roller=GameLogic.roll_dice):
        """
        This Function Is the Starting Point Of The Game, And It Will Keep The Game Running Until The Player Press q And
        Terminate The Game
        :param roller:
        :return: No output
        """

        self.welcome_msg()
        self.user_answer = input('> ')
        if self.user_answer == "n":
            print("OK. Maybe another time")

        else:
            self.user_answer = "r"
            while self.user_answer == "r" or self.user_answer == "b":
                new_roller = roller(self.dice_remaining)
                self.starting_round(new_roller)
                if self.user_answer == "q":
                    break
                self.bank()

            self.final_score_msg()

    @staticmethod
    def welcome_msg():
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")

    def roll_dices(self, roller):
        print(f"Rolling {self.dice_remaining} dice...")
        formatted_roller = " ".join([str(i) for i in roller])
        print(f"*** {formatted_roller} ***")

    def show_shelf_points_and_options(self):
        print(f"You have {self.banker.shelved} unbanked points and {self.dice_remaining} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")

    def banked_and_total_points_msg(self):
        print(f"You banked {self.banker.shelved} points in round {self.round_counter}")
        print(f"Total score is {self.banker.bank()} points")

    def final_score_msg(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")


if __name__ == "__main__":
    game = Game()
    game.play()
