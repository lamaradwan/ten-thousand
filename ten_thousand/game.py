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
        self.is_hot_dice = True
        self.banker = Banker()

    def starting_round(self, roller, roller_function=GameLogic.roll_dice):
        """
        | This Function Will Be Called In Each New Roll, A Tuple With Random Numbers Between 1 And 6 Will Be Passed To
        | This Function,The Tuple Length Depending On The Remaining Dices
        | :param roller:
        | :return: No output
        """
        roller = self.got_zilch(roller, roller_function)
        if len(roller) == 6 and self.is_hot_dice:
            print(f'Starting round {self.round_counter}')

        self.roll_dices(roller)
        print('Enter dice to keep, or (q)uit:')
        self.user_answer = input("> ")
        self.cheating_fix(roller)

    # Lama Radwan, Abdulrahman Mansour, Essa Abu Al-khair
    def cheating_fix(self, roller):
        if self.user_answer.isnumeric():
            userList = (list(map(int, self.user_answer)))
            # print(roller)
            for i in userList:
                if roller.count(i) < userList.count(i):
                    print("Cheater!!! Or possibly made a typo...")
                    formatted_roller = " ".join([str(i) for i in roller])
                    print(f"*** {formatted_roller} ***")
                    print('Enter dice to keep, or (q)uit:')
                    self.user_answer = input("> ")
                    return

    def bank(self):
        """
        This Function Will Called It Each Roll To Calculate The Total Score And Check If The Player Wants To Bank The
        Shelved Points Or Not
        :return: No Output
        """

        self.user_answer = (tuple(map(int, self.user_answer)))
        self.dice_remaining -= len(self.user_answer)
        self.banker.shelved += GameLogic.calculate_score(self.user_answer)
        print(f"You have {self.banker.shelved} unbanked points and {self.dice_remaining} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        self.user_answer = input("> ")

        if self.user_answer == "b":
            self.dice_remaining = 6
            self.is_hot_dice = True
            self.banked_and_total_points_msg()
            self.round_counter += 1

    def play(self, roller=GameLogic.roll_dice):
        """
        This Function Is the Starting Point Of The Game, And It Will Keep The Game Running Until The Player Press q And
        Terminate The Game
        :param roller:
        :return: No output
        """

        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        self.user_answer = input('> ')
        if self.user_answer == "n":
            print("OK. Maybe another time")

        else:
            while (self.user_answer == "r" or self.user_answer == "b" or self.user_answer == 'y') and (
                    self.round_counter < 21):
                new_roller = roller(self.dice_remaining)
                self.starting_round(new_roller, roller)
                if self.user_answer == "q":
                    break
                # if self.round_counter == 5:
                #     break
                ##Cheater method - possible
                # self.cheat(roller)
                self.bank()
                self.is_remaining_dices_zero()
            print(f"Thanks for playing. You earned {self.banker.balance} points")

    # def cheat_anf_fix(self, ):
    #     self.user_answer = (list(map(int, self.user_answer)))

    # Ahmad Zaid and Mohammad Abumazen
    def got_zilch(self, roll, roller_function):
        """
        This function will check if the rolling dice don't have any scoring dice, if yes zilch message will be printed
        to the player.

        This function take two parameters: roll: random tuple, roller_function: generate a new random tuple
        :param roll:
        :param roller_function:
        :return: random tuple
        """
        score = GameLogic.calculate_score(roll)
        if score == 0:
            self.roll_dices(roll)
            print("*" * 40)
            print("**        Zilch!!! Round over         **")
            print("*" * 40)
            self.banker.clear_shelf()
            self.banked_and_total_points_msg()
            self.dice_remaining = 6
            self.round_counter += 1
            new_roller = roller_function(6)
            return new_roller
        return roll

    def roll_dices(self, roller):
        print(f"Rolling {self.dice_remaining} dice...")
        formatted_roller = " ".join([str(i) for i in roller])
        print(f"*** {formatted_roller} ***")

    # def show_shelf_points_and_options(self):
    #     print(f"You have {self.banker.shelved} unbanked points and {self.dice_remaining} dice remaining")
    #     print("(r)oll again, (b)ank your points or (q)uit:")

    def banked_and_total_points_msg(self):
        print(f"You banked {self.banker.shelved} points in round {self.round_counter}")
        print(f"Total score is {self.banker.bank()} points")

    def is_remaining_dices_zero(self):
        if self.dice_remaining == 0:
            self.dice_remaining = 6
            self.is_hot_dice = False


if __name__ == "__main__":
    game = Game()
    game.play()
