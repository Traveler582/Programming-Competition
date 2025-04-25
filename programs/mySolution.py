#   Author: [Name]
#   Strategy_name: [Name]
#   [Basic rundown of strategy]

import random
from GameState import GameState

# Below is the stub file for your solution
# GameState is stored in the Gamemaster.Gamestate object
# This object has 2 properties of interest for the purposes of this game
# pmoves: previous player moves from previous rounds (always a 3xn array where the first index is the playerID and n is the number of rounds)
    # By convention playerID zero is always yourself
    # len(self.gs.pmoves[0]) gives the number of previous rounds
    # self.gs.pmoves[0][-1] gives your last move (note if this is the first round of the game this will error)
    # self.gs.pmoves[1][-1] and pmoves[2][-1] give other player 1 and other player 2s last move
    # self.gs.pmoves[0][5] gives your 6th move (renember how python arrays work). Be sure to confirm that 6 rounds have completed
# score: gives the current score of the game. (always an array of size 3 first index is the playerID)
    # self.gs.score[0] gives your current score
    # self.gs.score[1] and self.gs.score[2] gives the score of other player 1 and other player 2

# Game Scoring will be done exactly how the Gamemaster works but due note because of the random element runs of the Gamemaster are not deterministic
# Game rules are as follows
# ...



DEFECT = False
COOPERATE = True

class player:
    programName = "mySolution"
    programAuthor = "you"
    def __init__(self, gameState: GameState):
        self.gs = gameState

    def play(self):
        return COOPERATE