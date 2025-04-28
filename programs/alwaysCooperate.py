#   Author: [Name]
#   Strategy_name: [Name]
#   [Basic rundown of strategy]

DEFECT = False
COOPERATE = True

class player:
    programName = "alwaysCooperate"
    programAuthor = "Cooperateman"
    def __init__(self, gameState):
        self.gs = gameState

    def play(self):
        return COOPERATE