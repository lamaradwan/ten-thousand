import random


class GameLogic:

###################
#Calculate score method - Issa
###################


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

