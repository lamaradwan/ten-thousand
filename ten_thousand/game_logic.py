import random


class GameLogic:

    @staticmethod
    def calculate_score(args):
        args1=sorted(args)


        a1=args.count(1)==2
        a2=args.count(2)==2
        a3=args.count(3)==2
        a4=args.count(4)==2
        a5=args.count(5)==2
        a6=args.count(6)==2
        T=[a1,a2,a3,a4,a5,a6]



        cont = 0
        if args1 == [1, 2, 3, 4, 5, 6] or T.count(True)==3:
            cont = 1500

        else:
            if 0 <= args.count(1) < 3:
                cont += 100 * args.count(1)
            else:
                cont += 1000 * (args.count(1) - 2)
            if args.count(2) >= 3:
                cont += 200 * (args.count(2) - 2)
            if args.count(3) >= 3:
                cont += 300 * (args.count(3) - 2)
            if args.count(4) >= 3:
                cont += 400 * (args.count(4) - 2)
            if args.count(6) >= 3:
                cont += 600 * (args.count(6) - 2)

            if 0 <= args.count(5) < 3:
                cont += 50 * args.count(5)
            else:
                cont += 500 * (args.count(5) - 2)
        return cont


###################
#Roll-Dice method - Lama Radwan
    @staticmethod
    def roll_dice(num):
        tuple = ()
        for i in range(0, num):
            result = random.randint(1, 6)
            tuple = (*tuple, result)
        return tuple
###################

    @staticmethod
    def get_scorers(dice):
        # print(dice)
        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scores_list = []
        for i in range(len(dice)):
            sub_roll = dice[:i] + dice[i + 1:]
            sub_score = GameLogic.calculate_score(sub_roll)
            if sub_score != all_dice_score:
                scores_list.append(dice[i])

        return tuple(scores_list)

if __name__=="__main__":
    pass
    # print(GameLogic.calculate_score((1, 6, 3, 2, 5, 4)))
