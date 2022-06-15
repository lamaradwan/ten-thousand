from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        self.round_counter = 1

    def starting_round(self, round_counter, roller=GameLogic.roll_dice):
        print(f'Starting round {round_counter}')
        print('Rolling 6 dice...')
        new_roller = roller(6)
        formatted_roller = ' '.join([str(i) for i in new_roller])
        print(f'*** {formatted_roller} ***')
        print('Enter dice to keep, or (q)uit:')
        new_user_input = input("> ")
        return new_user_input

    def bank(self, banker, user_answer, round_counter):
        #Define the tuple to calculate the unbanked score
        user_answer_list = (tuple(map(int, user_answer)))
        unbanked_scored_points = GameLogic.calculate_score(user_answer_list)
        print(f"You have {unbanked_scored_points} unbanked points and 5 dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_answer = input("> ")
        if user_answer == "b":
            banker.shelf(unbanked_scored_points)
            print(f"You banked {banker.shelved} points in round {round_counter}")
            print(f"Total score is {banker.bank()} points")
            self.round_counter += 1
            self.starting_round(self.round_counter)
        return user_answer

    def play(self, roller=GameLogic.roll_dice):
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        user_answer = input('> ')
        if user_answer == 'n':
            print('OK. Maybe another time')
        else:
            new_user_input = self.starting_round(self.round_counter)
            banker = Banker()
            while new_user_input != "q":
                # new_roller_2 = roller(6)
                # bank one roll then quit -- Ahmad Zaid---Lama Radwan
                self.bank(banker, new_user_input, self.round_counter)
                while new_user_input == "q":
                    print(f'Thanks for playing. You earned {banker.balance} points')
                    break


if __name__ == '__main__':
    game = Game()
    game.play()
