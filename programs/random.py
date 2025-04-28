#   Author: [Name]
#   Strategy_name: [Name]
#   [Basic rundown of strategy]

import random

DEFECT = False
COOPERATE = True

class player:
    programName = "random"
    programAuthor = "alwaysRandom"
    def __init__(self, gameState):
        self.gs = gameState

    def play(self):
        return random.choice([DEFECT, COOPERATE])