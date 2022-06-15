from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        self.round_counter = 1

    def new_round(self, round_counter, banker, user_answer,new_roller_2, roller=GameLogic.roll_dice):
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
        print(f"Starting round {self.round_counter}")
        print('Rolling 6 dice...')
        # new_roller = roller(6)
        # roller=roller()
        formatted_roller = ' '.join([str(i) for i in new_roller_2])
        print(f'*** {formatted_roller} ***')
        print('Enter dice to keep, or (q)uit:')
        user_answer_2 = input('> ')

        return user_answer_2

    def play(self, roller=GameLogic.roll_dice):
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        user_answer = input('> ')
        if user_answer == 'n':
            print('OK. Maybe another time')
        else:
            # new_roller = roller(6)
            banker = Banker()
            print(f'Starting round {self.round_counter}')
            print('Rolling 6 dice...')
            new_roller = roller(6)
            formatted_roller = ' '.join([str(i) for i in new_roller])
            print(f'*** {formatted_roller} ***')
            print('Enter dice to keep, or (q)uit:')
            user_answer = input('> ')

            while user_answer != "q":
                new_roller_2 = roller(6)

                # bank one roll then quit -- Ahmad Zaid---Lama Radwan
                new_user_input = self.new_round(self.round_counter, banker, user_answer, new_roller_2)
                if new_user_input != 'r':
                    # here you should implement the repeat roller simulation file
                    break

            print(f'Thanks for playing. You earned {banker.balance} points')


if __name__ == '__main__':
    game = Game()
    game.play()
