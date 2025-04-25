#   Author: [Name]
#   Strategy_name: [Name]
#   [Basic rundown of strategy]

import random
import Gamemaster


DEFECT = False
COOPERATE = True

class player:
    programName = "copyLast"
    programAuthor = "copyCat"
    def __init__(self, gameState: Gamemaster.GameState):
        self.gs = gameState

    def play(self):
        # cooperate on the first round
        if len(self.gs.pmoves[0]) == 0:
            return COOPERATE
        else:
            # If other player 1 and other player 2 cooperated last round
            # also cooperate otherwise defect
            if self.gs.pmoves[1][-1] and self.gs.pmoves[2][-1]:
                return COOPERATE
            else:
                return DEFECT