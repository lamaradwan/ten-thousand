class Banker:

    ###################
    # Shelf method - Ahmad
    def __init__(self):
        self.shelved = 0
        self.balance = 0

    def shelf(self, un_banked_points: int):
        self.shelved += un_banked_points

    ###################
    # Bank method - Mohammad Abu mazen
    def bank(self):
        self.balance = 0
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    ###################
    # Clear Shelf method - Adbelrahman Refai
    def clear_shelf(self):
        self.shelved = 0
