from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        self.round_counter = 1
        self.dice_remaining = 6
        #############################
        # Ahmad And Lama

    def starting_round(self, round_counter, roller, roller_1=GameLogic.roll_dice):
        if len(roller) == 6:
            print(f'Starting round {round_counter}')
        print(f'Rolling {self.dice_remaining} dice...')
        new_roller = roller
        formatted_roller = ' '.join([str(i) for i in new_roller])
        print(f'*** {formatted_roller} ***')
        print('Enter dice to keep, or (q)uit:')
        new_user_input = input("> ")
        return new_user_input
        #############################

    #############################
    # Ahmad And Lama
    def bank(self, banker, user_answer, round_counter):
        # Define the tuple to calculate the unbanked score
        user_answer_list = (tuple(map(int, user_answer)))
        self.dice_remaining -= len(user_answer)
        unbanked_scored_points = GameLogic.calculate_score(user_answer_list)
        banker.shelved += unbanked_scored_points
        print(f"You have {banker.shelved} unbanked points and {self.dice_remaining} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_answer = input("> ")
        if user_answer == "b":
            self.dice_remaining = 6
            print(f"You banked {banker.shelved} points in round {round_counter}")
            print(f"Total score is {banker.bank()} points")
            self.round_counter += 1

        return user_answer

    #############################

    #############################
    # Ahmad And Lama
    def play(self, roller=GameLogic.roll_dice):
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        user_answer = input('> ')
        if user_answer == 'n':
            print('OK. Maybe another time')
        else:
            banker = Banker()
            new_user_input = ""
            x = ''
            while new_user_input != "q" and x != 'q':
                new_roller = roller(6)
                new_user_input = self.starting_round(self.round_counter, new_roller)
                if new_user_input == 'q':
                    break
                x = self.bank(banker, new_user_input, self.round_counter)
                if x == "r":
                    new_roller = roller(self.dice_remaining)
                    new_user_input = self.starting_round(self.round_counter, new_roller)
                    self.bank(banker, new_user_input, self.round_counter)
            print(f'Thanks for playing. You earned {banker.balance} points')

    #############################
    #############################

if __name__ == '__main__':
    game = Game()
    game.play()
