#   Author: [Name]
#   Strategy_name: [Name]
#   [Basic rundown of strategy]
import random

class player:
    def __init__(self, index):
        self.index = index

    def play(self, last_moves): # <LK>: Change the body of this function for your strategy!
        choice = random.choice([True, False])
        if choice == True:
            print("Random chooses: Cooperate")
        else:
            print("Random chooses: Defect")
        return choice