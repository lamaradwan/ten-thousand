from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        self.round_counter = 1
        #############################
        # Ahmad And Lama

    def starting_round(self, round_counter, roller, roller_1=GameLogic.roll_dice):
        print(f'Starting round {round_counter}')
        print('Rolling 6 dice...')
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
        unbanked_scored_points = GameLogic.calculate_score(user_answer_list)
        print(f"You have {unbanked_scored_points} unbanked points and 5 dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_answer = input("> ")
        if user_answer == "b":
            banker.shelf(unbanked_scored_points)
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

            print(f'Thanks for playing. You earned {banker.balance} points')
    #############################

    #############################

    # Mohammad and Abd

    def start_round(self, round, num_dice = 6):
        print(f"starting round {round}")

        round_score = 0

        while True:
            roll = self.roll_dice(num_dice)

            keepers = self.handle_keepers(roll)

            print("(r)oll again, (b)ank your points or (q)uit:")
            roll_again_response = input("> ")
            if roll_again_response == "q":

                self.quit_game()
                return

            elif roll_again_response == "b":

                round_score = self.banker.bank()

                break

            else:

                num_dice -= len(keepers)

                if num_dice == 0:
                    num_dice = 6

            print(f"You banked {str(round_score)} points in round {round}")


    def handle_keepers(self, roll):
        pass
    #############################

if __name__ == '__main__':
    game = Game()
    game.play()
