# Below is the documentation for the GameState object
# This is also included in the mySolution.py file
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
# Below is the source code for the GameState object
# You should not need to look at this for your solution and should only be concerned with pmoves & score
class GameState:
    def __init__(self, playerID, prevMoves, scores):
        self.pmoves = [None]
        self.score = [None]
        for i, (pmove, score) in enumerate(zip(prevMoves,scores)):
            if i == playerID:
                self.pmoves[0] = pmove
                self.score[0] = score
            else:
                self.pmoves.append(pmove)
                self.score.append(score)
    def updateScore(self, playerID, scores):
        offset = 1
        for i in range(len(scores)):
            if i == playerID:
                self.score[0] = scores[i]
                offset = 0
            else:
                self.score[i + offset] = scores[i]